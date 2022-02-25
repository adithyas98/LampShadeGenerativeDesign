import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

cube = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 0), scale=(0.1016, 0.1016, 0.0254))
cube = bpy.context.active_object
cyl = bpy.ops.mesh.primitive_cylinder_add(radius=0.1016, depth=0.0508,end_fill_type='NGON', align='WORLD', location=(0, 0, 0))
cyl = bpy.context.active_object
mod_bool = cube.modifiers.new('my_bool_mod', 'BOOLEAN')
mod_bool.operation = 'DIFFERENCE'
mod_bool.object = cyl
cyl.hide_set(True)
pillar1 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0.09652, 0.09652, -0.873), scale=(0.00508, 0.00508, -0.9238))
pillar1 = bpy.context.active_object
pillar2 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(-0.09652, -0.09652, -0.873), scale=(0.00508, 0.00508, -0.9238))
pillar2 = bpy.context.active_object
pillar3 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(-0.09652, 0.09652, -0.873), scale=(0.00508, 0.00508, -0.9238))
pillar3 = bpy.context.active_object
pillar4 = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0.09652, -0.09652, -0.873), scale=(0.00508, 0.00508, -0.9238))
pillar4 = bpy.context.active_object
roof = bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, -0.8222), scale=(0.1016, 0.1016, 0.0254))
roof = bpy.context.active_object
bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.09072200266506186, 0.0/2 + 0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.06049597396969009, 0.0/2 + 0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.08107905925420891, 0.0/2 + 0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.013791111828056757, 0.0/2 + 0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.02804884524516363, 0.0/2 + 0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.084533421138732, 0.0/2 + 0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.1016, 0.0/2 + 0.07282566053425371))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.1016, 0.0/2 + 0.06096730806818117))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.1016, 0.0/2 + 0.07117548628425333))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.1016, 0.0/2 + 0.05096089122233766))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.1016, 0.0/2 + 0.06803687997754038))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.1016, 0.0/2 + 0.04923606506051516))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.08121706489933142, 0.0/2 + -0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.035762834445639574, 0.0/2 + -0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.06401960617826805, 0.0/2 + -0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.011681050347434746, 0.0/2 + -0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.04710413815428714, 0.0/2 + -0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.10101380190710046, 0.0/2 + -0.1016, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.1016, 0.0/2 + 0.046908804919927716))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.1016, 0.0/2 + 0.038652048144465316))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.1016, 0.0/2 + 0.03694226949020374))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.1016, 0.0/2 + 0.028761967593851426))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.1016, 0.0/2 + 0.07353613727366329))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.1016, 0.0/2 + 0.032955188801344654))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.1016, 0.0/2 + 0.06439999939949312, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.1016, 0.0/2 + 0.07393134893222461, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.1016, 0.0/2 + 0.0816466234446881, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.1016, 0.0/2 + -0.09554574588170815, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.1016, 0.0/2 + -0.028896014713359328, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + -0.1016, 0.0/2 + 0.0072979326495091895, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.06084593096570809))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.062244862412286564))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.07179027564072714))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.04620352090220226))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.07603841123036155))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.06861567185408185))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.1016, 0.0/2 + -0.062488151052556014, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.1016, 0.0/2 + 0.03162094836747362, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.1016, 0.0/2 + -0.013632281662747395, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.1016, 0.0/2 + -0.017005723385903143, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.1016, 0.0/2 + -0.09805655934035093, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.05079999999999999,location = (0.0/2 + 0.1016, 0.0/2 + 0.08911216464098581, 0.05079999999999999/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.07526243563149376))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.06213278899291989))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.07011663730814005))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.055572234385471916))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.026657247977846108))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.1016, 0.2032/2 + -0.1016, 0.0/2 + 0.03673103652466101))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.0465908052392897, 0.2032/2 + -0.1016, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.08221546423349528, 0.2032/2 + -0.1016, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.07421939423858814, 0.2032/2 + -0.1016, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.04747995353220824, 0.2032/2 + -0.1016, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.07448615418141119, 0.2032/2 + -0.1016, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + 0.09357856698495859, 0.2032/2 + -0.1016, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.01732499576724475, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.051471250351029174, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.062464740318389694, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.05286285503243271, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.09180501119961307, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.03554894241165378, 0.0/2 + 0.07619999999999999))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.05461882157976554, 0.2032/2 + -0.1016, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.06116386178548246, 0.2032/2 + -0.1016, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.0727561075950757, 0.2032/2 + -0.1016, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.0043890384920275555, 0.2032/2 + -0.1016, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.08467172139861269, 0.2032/2 + -0.1016, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.0/2 + -0.08731966824382023, 0.2032/2 + -0.1016, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 1.5707963267948966

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.0637933312327453, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + 0.061145124090805886, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.06929551585562661, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.05407599994027361, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.03230362416586047, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.mesh.primitive_cylinder_add(radius = 0.001,depth = 0.2032,location = (0.2032/2 + -0.1016, 0.0/2 + -0.09060181136279298, 0.0/2 + 0.0254))
bpy.context.object.rotation_euler[1] = 1.5707963267948966
bpy.context.object.rotation_euler[2] = 0.0

bpy.ops.wm.save_mainfile(filepath='./shade.blend')
bpy.ops.export_mesh.stl(filepath='./shade.stl')