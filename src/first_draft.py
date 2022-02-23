import bpy
from random import randint

#clear the workspace
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#building the base with cutout for lamp
bpy.ops.mesh.primitive_cube_add(location=(0,0,0), scale = (100, 100, 5))
cube = bpy.context.active_object
bpy.ops.mesh.primitive_cylinder_add(radius=15, depth=10, location=(0,0,0))
cyl = bpy.context.active_object

mod_bool = cube.modifiers.new('my_bool_mod', 'BOOLEAN')
mod_bool.operation = 'DIFFERENCE'
mod_bool.object = cyl

cyl.hide_set(True)


#vertical "pillars"
bpy.ops.mesh.primitive_cube_add(location=(95,95,55), scale = (5, 5, 50))
cube2 = bpy.context.active_object

bpy.ops.mesh.primitive_cube_add(location=(-95,-95,55), scale = (5, 5, 50))
cube3 = bpy.context.active_object

bpy.ops.mesh.primitive_cube_add(location=(95,-95,55), scale = (5, 5, 50))
cube4 = bpy.context.active_object

bpy.ops.mesh.primitive_cube_add(location=(-95,95,55), scale = (5, 5, 50))
cube5 = bpy.context.active_object

#horizontal top "beams"
bpy.ops.mesh.primitive_cube_add(location=(95,0,110), scale = (5, 100, 5))
cube6 = bpy.context.active_object

bpy.ops.mesh.primitive_cube_add(location=(-95,0,110), scale = (5, 100, 5))
cube7 = bpy.context.active_object

bpy.ops.mesh.primitive_cube_add(location=(0,95,110), scale = (90, 5, 5))
cube8 = bpy.context.active_object

bpy.ops.mesh.primitive_cube_add(location=(0,-95,110), scale = (90, 5, 5))
cube9 = bpy.context.active_object


#let's try some random extrusions in vertical direction
for i in range(1,5):
    x = randint(-90,90)
    bpy.ops.mesh.primitive_cube_add(location=(x,95,55), scale = (5, 5, 50))
    
for i in range(1,5):
    x = randint(-90,90)
    bpy.ops.mesh.primitive_cube_add(location=(x,-95,55), scale = (5, 5, 50)) 
    
for i in range(1,5):
    y = randint(-90,90)
    bpy.ops.mesh.primitive_cube_add(location=(95,y,55), scale = (5, 5, 50))
    
for i in range(1,5):
    y = randint(-90,90)
    bpy.ops.mesh.primitive_cube_add(location=(-95,y,55), scale = (5, 5, 50))
    

#let's try some random extrusions in horizontal direction
rot = 3.14/2

for i in range(1,4):
    z = randint(10,100)
    bpy.ops.mesh.primitive_cylinder_add(radius=5, depth=200, location=(95,0,z), rotation=(rot,0,0))

for i in range(1,4):
    z = randint(10,100)
    bpy.ops.mesh.primitive_cylinder_add(radius=5, depth=200, location=(-95,0,z), rotation=(rot,0,0))
    
for i in range(1,4):
    z = randint(10,100)
    bpy.ops.mesh.primitive_cylinder_add(radius=5, depth=200, location=(0,95,z), rotation=(rot,0,rot))
    
for i in range(1,4):
    z = randint(10,100)
    bpy.ops.mesh.primitive_cylinder_add(radius=5, depth=200, location=(0,-95,z), rotation=(rot,0,rot))    


bpy.ops.export_mesh.stl('INVOKE_DEFAULT',filepath='./test.stl')
