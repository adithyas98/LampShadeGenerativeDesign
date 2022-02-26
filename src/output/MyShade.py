import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

cube = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 0), scale=(0.0635, 0.0635, 0.02032))
cube = bpy.context.active_object
cyl = bpy.ops.mesh.primitive_cylinder_add(radius=0.047625, depth=0.04064,end_fill_type='NGON', align='WORLD', location=(0, 0, 0))
cyl = bpy.context.active_object
mod_bool = cube.modifiers.new('my_bool_mod', 'BOOLEAN')
mod_bool.operation = 'DIFFERENCE'
mod_bool.object = cyl
cyl.hide_set(True)
pillar1 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0.06096, 0.06096, 0.050291999999999996), scale=(0.00254, 0.00254, 0.029971999999999995))
pillar1 = bpy.context.active_object
pillar2 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(-0.06096, -0.06096, 0.050291999999999996), scale=(0.00254, 0.00254, 0.029971999999999995))
pillar2 = bpy.context.active_object
pillar3 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(-0.06096, 0.06096, 0.050291999999999996), scale=(0.00254, 0.00254, 0.029971999999999995))
pillar3 = bpy.context.active_object
pillar4 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0.06096, -0.06096, 0.050291999999999996), scale=(0.00254, 0.00254, 0.029971999999999995))
pillar4 = bpy.context.active_object
roof = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 0.080772), scale=(0.0635, 0.0635, 0.001016))
roof = bpy.context.active_object
bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.04420917881834212, 0.0/2 + 0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.0031297510336675202, 0.0/2 + 0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.02281026366447763, 0.0/2 + 0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + 0.03153137972929794, 0.0/2 + 0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.0532606591482866, 0.0/2 + 0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.05310165949882288))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.0743357855490119))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.060545473915281714))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.05297288265766015))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.06680911325710102))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.04176753747069534, 0.0/2 + -0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.03785472081828864, 0.0/2 + -0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.051713868128652536, 0.0/2 + -0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.004217100967708366, 0.0/2 + -0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + 0.006980928990909699, 0.0/2 + -0.0635, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.05929877184910512))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.034223291350013355))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.04842812547934082))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.030369733032201415))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.04900210509715934))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.0635, 0.0/2 + -0.030987100053527894, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.0635, 0.0/2 + 0.04728538189076188, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.0635, 0.0/2 + -0.02741496599637632, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.0635, 0.0/2 + -0.0016764385603470142, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + -0.0635, 0.0/2 + -0.060916666682913435, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.04055137762529934))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.048286313619961954))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.039889799834145215))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.07831386410693356))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.04331486126842242))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + 0.0635, 0.0/2 + 0.06276669440886262, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + 0.0635, 0.0/2 + -0.05182333012142174, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + 0.0635, 0.0/2 + 0.05640736825456974, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + 0.0635, 0.0/2 + 0.005540349868992059, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.060959999999999986,location = (0.0/2 + 0.0635, 0.0/2 + -0.048272336607819766, 0.060959999999999986/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.06994955997477022))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.08059940713905252))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.03484952523298403))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.035391045096806295))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.045614874844452716))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.wm.save_mainfile(filepath='./shade.blend')
bpy.ops.export_mesh.stl(filepath='./shade.stl')