"""Change one thing: repaint the Ball from blue to orange, and save
the scene under a new name so both versions exist side by side.

    blender -b still-life.blend --python recolour_ball.py
"""

import os

import bpy

mat = bpy.data.materials["BallBlue"]
bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
colour = bsdf.inputs["Base Color"].default_value
print("=== recolour_ball ===")
print("Before: material %s base colour = %s" % (mat.name, tuple(round(c, 3) for c in colour[:3])))

colour[0], colour[1], colour[2] = 1.0, 0.45, 0.05  # orange
# Keep the viewport colour in step, as build_scene.py does, so the
# Workbench engine agrees with Cycles about the new colour.
mat.diffuse_color = (1.0, 0.45, 0.05, 1.0)
mat.name = "BallOrange"
print("After:  material %s base colour = %s" % (mat.name, tuple(round(c, 3) for c in colour[:3])))

out = os.path.join(os.getcwd(), "still-life-orange.blend")
bpy.ops.wm.save_as_mainfile(filepath=out)
print("Saved:", out)
print("=== end ===")
