"""Print what is in the current scene: Blender's version, every
object with its type and location, and every material with its
base colour. Run it in background mode:

    blender -b somefile.blend --python inspect_scene.py
    blender -b --python inspect_scene.py        (factory scene)
"""

import bpy


def base_colour(material):
    """The Base Color of a material's Principled BSDF, or None."""
    if not material or not material.use_nodes:
        return None
    for node in material.node_tree.nodes:
        if node.type == "BSDF_PRINCIPLED":
            rgba = node.inputs["Base Color"].default_value
            return tuple(round(c, 3) for c in rgba[:3])
    return None


print("=== inspect_scene ===")
print("Blender version:", bpy.app.version_string)
scene = bpy.context.scene
print("Scene name:", scene.name)
print("Render engine:", scene.render.engine)
print("Resolution: %d x %d" % (scene.render.resolution_x,
                               scene.render.resolution_y))
print("Camera:", scene.camera.name if scene.camera else "NONE")

print("\nObjects (%d):" % len(scene.objects))
for obj in scene.objects:
    loc = tuple(round(v, 2) for v in obj.location)
    print("  %-12s type=%-8s location=%s" % (obj.name, obj.type, loc))

print("\nMaterials (%d):" % len(bpy.data.materials))
for mat in bpy.data.materials:
    print("  %-12s base colour=%s" % (mat.name, base_colour(mat)))
print("=== end ===")
