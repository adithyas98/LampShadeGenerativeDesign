
import bpy #Python module for Blender

class Blender:
    '''
    This class will implement all the necessary Blender methods
    '''
    
    def __init__(self):
        self.debug = True #simple debug variable
            
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
        bpy.ops.export_mesh.stl(filepath=filepath)
