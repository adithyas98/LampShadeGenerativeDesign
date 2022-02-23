#!/usr/bin/env python3

from BlenderClass import Blender
from UIClass import UserInput
from ShapewaysAPI import ShapeWayAPI

import os
import random

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
        #create the blender object
        self.blender = Blender()

    def face(self,coordinates,iterations):
        '''
        This method will randomly create a grid pattern on a face that is 
        passed in through the coordinates
        Inputs:
            - coordinates: a list of tuples that express the four points that 
                            bound the face
                            ex. [(x1,y1,z1), ... , (x4,y4,z4)]
            - iterations: A standin for the complexity of the faces. Basically,
                            the number of random lines that are drawn on the 
                            face.
        Output:
            - a list of x,y and z coordinates that define the grid pattern on 
                        the face
            - a list of random coordinates generated
        '''
        #Check that there are only 4 points
        assert len(coordinates) == 4, "Four points were not passed!"
        #First make sure the coordinates that are passed are of the same length
        variables = len(coordinates[0])
        for c in coordinates:
            assert len(c) == variables
        #first we need to find the coordinate that is unchanging on the face
        constantIdx = 0 #Will hold the constant id
        for i in len(coordinates[0]):
            m = coordinates[0][i]
            if m == coordinates[1][i] and m == coordinates[2][i]:
                #Then we have found out constant coordinate
                constantIdx = i
                break
        #Create lists to hold the max and min values for each dimension
        maxValues = [] 
        minValues = []
        for dim in range(len(coordinates[0])):
            #find the max within that coordinate
            dimVars = [] #will hold all of the values of the dim
            for c in coordinates:
                dimVars.append(c[dim]) #Append the value at that dim
            #find the min and max
            maxValues.append(max(dimVars))
            minValues.append(min(dimVars))
        generatedDims = [[],[],[]] 
        #Now we can make lines along each axis
        for dim in range(len(coordiantes[0])):
            if dim == constantIdx:
                #continue to the next iteration if we have the constant index
                continue
            else:
                #we can make our random grid lines
                for i in range(iterations/2):
                    #find the two coordinates to create the cylinder
                    randPoint = minValues[dim]+(maxValues[dim]-minValues[dim])*random.random()

                    #Add the generated point to the correct list
                    generatedDims[dim].append(randPoint)
                    #Create the points
                    #Init them with noticable points
                    point0 = [None,None,None] 
                    point1 = [None,None,None] 

                    #Add the random point
                    point0[dim] = randPoint
                    point1[dim] = randPoint
                    #Add the constant point
                    point0[constantIdx] = coordinates[0][constantIdx]
                    point1[constantIdx] = coordinates[0][constantIdx]

                    #other dimension taking into account the min and max
                    #find the dim of the other dim by finding the none
                    other = point0.index(None)
                    point0[other] = minValues[other]
                    point1[other] = maxValues[other]

                    #now make the cylinder
                    self.blender.cylinderBetween(point0,point1,radius=2)
        return generatedDims
    def linesBetweenFaces(self,face0,face1,points0,points1):
        '''
        Randomly generates cylinders between the points listed on the face
        Inputs:
            - face0: list of four points that defines first face
            - face1: list of four points that defines the second face
            - points0: list of points that defines the grid on face 1
            - points1: list of points that defines the grid on face 2
        Output:
            - Rendomly generated cylinders
        '''



                    
                    


        

        











