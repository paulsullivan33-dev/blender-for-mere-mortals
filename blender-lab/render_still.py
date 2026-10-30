"""Render frame 1 of the loaded scene with a chosen engine.

    blender -b still-life.blend --python render_still.py -- ENGINE SAMPLES OUTPUT.png

ENGINE is one of CYCLES, BLENDER_EEVEE_NEXT, BLENDER_WORKBENCH.
SAMPLES applies to Cycles only (ignored by the other engines).
"""

import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
engine, samples, output = argv[0], int(argv[1]), argv[2]

scene = bpy.context.scene
scene.render.engine = engine
if engine == "CYCLES":
    scene.cycles.device = "CPU"
    scene.cycles.samples = samples
scene.render.filepath = output
scene.frame_set(1)

print("=== render_still ===")
print("Engine:", engine, "| Cycles samples:", samples if engine == "CYCLES" else "n/a")
print("Output:", output)
bpy.ops.render.render(write_still=True)
print("=== render done ===")
