#!/usr/bin/env python3
import math
class Blender:
    '''
    This class will implement all the necessary Blender methods
    '''
    
    def __init__(self):
        self.debug = True #simple debug variable
            
    def clear(self):
        '''
        This method will clear the workspace
        '''
        clear = "bpy.ops.object.select_all(action='SELECT')\n"
        clear += "bpy.ops.object.delete(use_global=False)\n"
        return clear
    def header(self):
        '''
        Will add the import statement
        '''
        return "import bpy\n"
    
    def cube(self, x, y, z, sx, sy, sz):
        '''
        This will create a cube with desired inputs
        Inputs:
            - size: size of the cube
            - x: location on x axis
            - y: location on y axis
            - z: location on z axis
            - rx: rotation about x
            - ry: rotation about y
            - rz: rotation about z
            - sx: scale factor along x
            - sy: scale factor along y
            - sz: scale factor along z
        Output:
            - creates a cube with desired parameters
        '''

        cube = "bpy.ops.mesh.primitive_cube_add(align='WORLD', "
        cube += "location=({}, {}, {}), ".format(x,y,z)
        cube += "scale=({}, {}, {}))".format(sx,sy,sz)
        
        return cube

    def cylinderBetween(self,point0,point1,radius):
        '''
        Will create a cylinder between two points with the specified radius
        Inputs:
           - point0: a tuple containing x,y,z coordinates for the first point
           - point1: a tuple containing x,y,z coordinates for the second point
           - radius: the radius of the cylinder
        output:
            - The cylinder object added to the cavnas
        '''
        x1 = point0[0]
        x2 = point1[0]
        y1 = point0[1]
        y2 = point1[1]
        z1 = point0[2]
        z2 = point1[2]
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        dist = math.sqrt(dx**2 + dy**2 + dz**2)

        cyl = 'bpy.ops.mesh.primitive_cylinder_add(radius = {},depth = {},'.format(radius,dist)
        cyl += 'location = ({}/2 + {}, {}/2 + {}, {}/2 + {}))\n'.format(dx,x1,dy,y1,dz,z1)

        phi = math.atan2(dy, dx)
        theta = math.acos(dz/dist)

        cyl += 'bpy.context.object.rotation_euler[1] = {}\n'.format(theta)
        cyl += 'bpy.context.object.rotation_euler[2] = {}\n'.format(phi)            
        return cyl

            
    def cylinder(self, r, d, x, y, z):
        '''
        This will create a cylinder with desired inputs
        Inputs:
            - v: vertices used to build cylinder
            - r: radius of cylinder
            - d: depth of cylinder
            - x: location on x axis
            - y: location on y axis
            - z: location on z axis
            - rx: rotation about x
            - ry: rotation about y
            - rz: rotation about z
            - sx: scale factor along x
            - sy: scale factor along y
            - sz: scale factor along z
        Output:
            - creates a cylinder with desired parameters
        '''
        cylinder = "bpy.ops.mesh.primitive_cylinder_add"
        cylinder += "(radius={}, depth={},".format(r,d)
        cylinder += "end_fill_type='NGON', align='WORLD', "
        cylinder += "location=({}, {}, {}))".format(x,y,z) 
        
        return cylinder
                                                        
    def exportSTL(self,filepath):
        '''
        Export the stl file of the object that was created
        Input:
            - filepath: The full filepath to where you want to save the stl file Output:
            - Confirmation that the file was saved
        '''
        export = "bpy.ops.export_mesh.stl(filepath='{}')".format(filepath)
        
        return export
    
    def currentObject(self, mesh):
        '''
        Assigns blender mesh on screen to current object 

        '''
        currentObject = "{} = bpy.context.active_object".format(mesh)
        
        return currentObject
    
    def blenderUnitsToInches(self,bu):
        '''
        Converts Blender units (BU) to inches
        Inputs:
            - bu: blender units to convert
        Output:
            - conversion made to inches(float)
        '''
        #1in = 0.0254 bu
        return bu/0.0254
    def inchesToBlenderUnits(self,inches):
        '''
        Converts inches to Blender Units. Trusts that the scale has not been
        changed!!!
        Inputs:
            - inches: inches measurement to convert
        Outputs:
            - Converted measurement in blender units (bu)
        '''
        #1in = 0.0254 bu
        return inches * 0.0254
    def saveBlendFile(self,filename):
        '''
        Saves the model as a blend file
        Input:
            - filename: full file path where you want to save the file
        Ouput:
            - the command to save the file
        '''
        return "bpy.ops.wm.save_mainfile(filepath='{}')".format(filename)
