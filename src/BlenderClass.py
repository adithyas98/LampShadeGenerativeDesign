#!/usr/bin/env python3

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
    def header(self):
        '''
        Will add the import statement
        '''
        return "import bpy"
    
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
        cube += "location=({}, {}, {}), rotation=(rx, ry, rz),".format(x,y,z,rx,ry,rz)
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
            - filepath: The full filepath to where you want to save the stl file Output:
            - Confirmation that the file was saved
        '''
        export = "bpy.ops.export_mesh.stl(filepath={})".format(filepath)
        
        return export
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
        return "bpy.ops.wm.save_mainfile(filename={})".format(filename)
