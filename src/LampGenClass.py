#!/usr/bin/env python3

from BlenderClass import Blender
from UIClass import UserInput
from ShapewaysAPI import ShapeWayAPI
from random import randint

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
        intro = "Please answer the following questions. All answers are in inches"
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

        #Create a list to hold the commands
        self.lampCmds = []

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
                    self.lampCmds.append(self.blender.cylinderBetween(point0,point1,radius=1))
        return generatedDims
    def linesBetweenFaces(self,face0,face1,points0,points1,iterations):
        '''
        Randomly generates cylinders between the points listed on the face
        Inputs:
            - face0: list of four points that defines first face
            - face1: list of four points that defines the second face
            - points0: list of points that defines the grid on face 1
            - points1: list of points that defines the grid on face 2
            - iterations: A proxy for the complexity of the model
                            -The number of random cylinders drawn
        Output:
            - Rendomly generated cylinders
        '''
        #find the common coordinate for each face
        commonIdxs = []
        for face in [face0,face1]:
            for i in len(faces[0]):
                m = faces[0][i]
                if m == faces[1][i] and m == faces[2][i]:
                    #Then we have found out constant coordinate
                    constantIdx.append(i)
                    break
        assert len(commonIdxs) == 2 #Want to make sure we have two faces!
        for i in range(iterations + 1):
            #Init the point lists with something noticable
            p0 = [None,None,None]
            p1 = [None,None,None]
            #add the constant coordinates to each
            p0[commonIdxs[0]] = face0[commonIdx[0]]
            p1[commonIdxs[1]] = face1[commonIdx[1]]

            #Add the random coordinate for face0
            for dim in range(len(points0)):
                if len(points0[dim]) == 0:
                    continue
                else:
                    #We want to generate a point here
                    p0[dim] = random.choice(points0[dim])
             #Do the same for point 1
            for dim in range(len(points1)):
                if len(points1[dim]) == 0:
                    continue
                else:
                    #We want to generate a point here
                    p1[dim] = random.choice(points1[dim])
                                       
            #now we can create the cylinder
            self.lampCmds.append(self.blender.cylinderBetween(p0,p1,radius=1))

                
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
        vp_y =  base_w/2 - vp_t/2 #absolute value of pillar y coordinates
        
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
    def exportLampShade(self,filename):
        '''
        Method that will export the lamp shade as an stl file
        Input:
            - None
        Output:
            - stl file of lamp shade
        '''
        #Start creating the file
        #first call the base class
        self.base()
        





        #Now we can export the stl file
        self.blender.exportSTL(filename)
        
        






