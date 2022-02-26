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
pillar1 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0.060325000000000004, 0.060325000000000004, 0.062865), scale=(0.0031750000000000003, 0.0031750000000000003, 0.042545))
pillar1 = bpy.context.active_object
pillar2 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(-0.060325000000000004, -0.060325000000000004, 0.062865), scale=(0.0031750000000000003, 0.0031750000000000003, 0.042545))
pillar2 = bpy.context.active_object
pillar3 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(-0.060325000000000004, 0.060325000000000004, 0.062865), scale=(0.0031750000000000003, 0.0031750000000000003, 0.042545))
pillar3 = bpy.context.active_object
pillar4 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0.060325000000000004, -0.060325000000000004, 0.062865), scale=(0.0031750000000000003, 0.0031750000000000003, 0.042545))
pillar4 = bpy.context.active_object
roof = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 0.106045), scale=(0.0635, 0.0635, 0.00127))
roof = bpy.context.active_object
bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.020401291898316153, 0.0/2 + 0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.024568192078087782, 0.0/2 + 0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.05677286722856853, 0.0/2 + 0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.046826124217800885, 0.0/2 + 0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.031152765360876356, 0.0/2 + 0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.09534200710533841))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.031394315372962646))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.08482937422132718))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.04105038962114846))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + 0.0635, 0.0/2 + 0.03292664296702435))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.010766257688080538, 0.0/2 + -0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.016645820160165532, 0.0/2 + -0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.02714343224039962, 0.0/2 + -0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.04996771439808921, 0.0/2 + -0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.027073991429972057, 0.0/2 + -0.0635, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.03912974453917893))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.039209116860418516))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.05938815852181595))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.07671793006949923))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.127/2 + -0.0635, 0.0/2 + -0.0635, 0.0/2 + 0.07562068764075525))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.0635, 0.0/2 + -0.007568964005884089, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.0635, 0.0/2 + -0.006166275095434312, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.0635, 0.0/2 + -0.04801129358932156, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.0635, 0.0/2 + 0.04871749852059935, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + -0.0635, 0.0/2 + -0.0050783801512373355, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.07481345654537275))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.09178483017816871))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.04053733098066349))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.03812870526892303))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + -0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.06100391561696257))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.0635, 0.0/2 + 0.05996852885873348, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.0635, 0.0/2 + -0.043545362363130585, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.0635, 0.0/2 + 0.02905247458243798, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.0635, 0.0/2 + -0.017244181065595637, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.08635999999999999,location = (0.0/2 + 0.0635, 0.0/2 + 0.04305378013857418, 0.08635999999999999/2 + 0.02032))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.10314442876987004))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.03757210825744254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.09496449089535106))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.08867596395305931))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.127,location = (0.0/2 + 0.0635, 0.127/2 + -0.0635, 0.0/2 + 0.051325830038279785))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.wm.save_mainfile(filepath='./shade.blend')
bpy.ops.export_mesh.stl(filepath='./shade.stl')