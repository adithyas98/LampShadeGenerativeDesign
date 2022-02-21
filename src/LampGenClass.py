#!/usr/bin/env python3

from BlenderClass import Blender
from UIClass import UserInput
from ShapewaysAPI import ShapeWayAPI

import os

class LampGen:
    '''
    This class will use the blender class to build the lamp shade and generate
    and stl file.
    '''

    def __init__(self,csvInput=False,csvFile=None):
        '''
        Inputs:
            - csvInput: (Boolean). True if the user wants to input dimensions with a csv file
            - csvFile: the full filepath to the csv file (String)
        '''
        #Define the intro to the questions
        intro = "Please answer the following questions. All answers are in cm"
        qdata = dict()
        #Get the Dimensions of the Lamp
        #Diameter of the lamp
        qdata['d']['question'] = "What is the diameter of the Lamp?"
        qdata['d']['convert'] = float

        #Height of the Lamp
        qdata['lampHeight']['question'] = "What is the height of the Lamp?"
        qdata['lampHeight']['convert'] = float

        #Ask for MAX Price
        qdata['price']['question'] = "What is the maximum price you want to spend?"
        qdata['price']['convert'] = float

        #Ask for Dims of Lampshade
        #height
        qdata['height']['question'] = "What is the height of the Lamp Shade?"
        qdata['height']['convert'] = float
        #Width
        qdata['width']['question'] = "What is the width of the Lamp Shade?"
        qdata['width']['convert'] = float
        #Length
        qdata['length']['question'] = "What is the length of the Lamp Shade?"
        qdata['length']['convert'] = float
        

        #Create a ui object and ask the questions
        ui = UserInput(qdata,intro)
        
        #Now set up a control flow for csv I/O
        if csvInput:
            #then the user wants to use a csv file
            if os.path.exists(csvFile):
                #Then we want to import the data
                self.qdata = ui.inputCSV(csvFile)
            else:
                #Then we want to output a csv file
                ui.outputQuestions(csvFile)
        else:
            #If the user doesn't want to use csv input
            #  Then we just want to ask the questions
            self.qdata = ui.askQuestions()


        











