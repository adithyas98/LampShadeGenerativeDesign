#!/usr/bin/env python3

from BlenderClass import Blender
from UIClass import UserInput
from ShapewaysAPI import ShapeWayAPI
from random import randint

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
                
    def Base(self):
        '''
        This class will take dimensions from UIclass to build the base
        '''
        
        #roof thickness
        roof_t = 1
        
        #pulling in dimensions from UIclass
        lamp_r = self.qdata['d']['data'] #radius of lamp
        lamp_h = self.qdata['lampHeight']['data'] #depth of lamp
        base_l = self.qdata['length']['data'] #length of base
        base_w = self.qdata['width']['data'] #width of base
        base_h = lamp_h #height of base
        H = self.qdata['height']['data'] #overall height

        
        #building the base with cutout for lamp
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0), scale = (base_l/2, base_w/2, base_h/2))
        cube = bpy.context.active_object
        bpy.ops.mesh.primitive_cylinder_add(radius=lamp_r, depth=lamp_h, location=(0,0,0))
        cyl = bpy.context.active_object
        
        mod_bool = cube.modifiers.new('my_bool_mod', 'BOOLEAN')
        mod_bool.operation = 'DIFFERENCE'
        mod_bool.object = cyl
        
        cyl.hide_set(True)
        
        
        #vertical "pillars"
        vp_h = H - roof_t - base_h #height of pillar
        vp_Zcenter = base_h + vp/2 #Z-coordinate of pillat centroid
        vp_t = 0.05*H #thickness of pillar aka cross section width
        vp_x =  base_l/2 - vp_t/2 #absolute value of pillar x coordinates
        vp_y =  base_l/2 - vp_t/2 #absolute value of pillar y coordinates
        
        bpy.ops.mesh.primitive_cube_add(location=(vp_x,vp_y,vp_Zcenter), scale = (vp_t/2, vp_t/2, vp_h/2))
        cube2 = bpy.context.active_object
        
        bpy.ops.mesh.primitive_cube_add(location=(-1*vp_x,-1*vp_y,vp_Zcenter), scale = (vp_t/2, vp_t/2, vp_h/2))
        cube3 = bpy.context.active_object
        
        bpy.ops.mesh.primitive_cube_add(location=(-1*vp_x,vp_y,vp_Zcenter), scale = (vp_t/2, vp_t/2, vp_h/2))
        cube4 = bpy.context.active_object
        
        bpy.ops.mesh.primitive_cube_add(location=(vp_x,-1*vp_y,vp_Zcenter), scale = (vp_t/2, vp_t/2, vp_h/2))
        cube5 = bpy.context.active_object
                
        #roof
        roof_Zcenter = H - base_h/2 - roof_t/2
        bpy.ops.mesh.primitive_cube_add(location=(0,0,roof_Zcenter), scale = (base_l/2, base_w/2, base_h/2))
        cube6 = bpy.context.active_object
        
        






