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
        clear = "bpy.ops.object.select_all(action='SELECT')"
        clear += "bpy.ops.object.delete(use_global=False)"
        return clear
    
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
        cube = "bpy.ops.mesh.primitive_cube_add(size={}, align='WORLD', ".format(size)
        cube += "location=({}, {}, {}), rotation=(rx, ry, rz),"format(x,y,z,rx,ry,rz)
        cube += "scale=(sx, sy, sz))".format(sx,sy,sz)
        
        return cube
            
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
        cylinder = "bpy.ops.mesh.primitive_cylinder_add"
        cylinder += "(vertices={}, radius={}, depth={},".format(v,r,d)
        cylinder += "end_fill_type='NGON', align='WORLD', "
        cylinder += "location=({}, {}, {}), rotation=({}, {}, {}),".format(x,y,z,rx,ry,rz) 
        cylinder += "scale=({}, {}, {}))".format(sz,sy,sz)
        
        return cylinder
                                                        
    def exportSTL(self,filepath):
        '''
        Export the stl file of the object that was created
        Input:
            - filepath: The full filepath to where you want to save the stl file
        Output:
            - Confirmation that the file was saved
        '''
        export = "bpy.ops.export_mesh.stl(filepath={})".format(filepath)
        
        return export
