#!/usr/bin/env python3
import bpy #Python module for Blender

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
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
    
    def cube(self, size, x, y, z, rx, ry, rz, sx, sy, sz):
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
        bpy.ops.mesh.primitive_cube_add(size=size, align='WORLD', \
                                        location=(x, y, z), rotation=(rx, ry, rz), scale=(sx, sy, sz))
            
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
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        dist = math.sqrt(dx**2 + dy**2 + dz**2)

        bpy.ops.mesh.primitive_cylinder_add(radius = r,depth = dist,
              location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)
        )

        phi = math.atan2(dy, dx)
        theta = math.acos(dz/dist)

        bpy.context.object.rotation_euler[1] = theta
        bpy.context.object.rotation_euler[2] = phi

    def cylinder(self, v, r, d, x, y, z, rx, ry, rz, sx, sy, sz):
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
        bpy.ops.mesh.primitive_cylinder_add(vertices=v, radius=r, depth=d, \
                                            end_fill_type='NGON', align='WORLD', location=(x, y, z), rotation=(rx, ry, rz), scale=(sx, sy, sz))            
    def exportSTL(self,filepath):
        '''
        Export the stl file of the object that was created
        Input:
            - filepath: The full filepath to where you want to save the stl file
        Output:
            - Confirmation that the file was saved
        '''
        bpy.ops.export_mesh.stl('INVOKE_DEFAULT',filepath='./test.stl')
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
    def exportImage(self,filepath):
        '''
        #TODO: UNTESTED !!!! PLEASE TEST!
        Will export an image of the object
        Input:
            - filepath: The filepath to save the image file
        '''
        bpy.context.scene.render.filepath = filepath
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.ops.object.camera_add(location=(0, 4, 4),rotation=(-0.7853, 0, 0))
        context.scene.camera = context.object 
        bpy.context.render.render(write_still=True)

