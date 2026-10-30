"""Build this guide's example scene from nothing: a still life of
simple shapes on a ground plane, with a sun light and a camera.
Saves the scene as still-life.blend next to this script's working
directory and prints an inventory of what it made.

    blender -b --python build_scene.py
"""

import math
import os

import bpy
from mathutils import Vector


def look_at(obj, point):
    """Aim an object's -Z axis (a camera's viewing direction) at a
    point in space."""
    direction = Vector(point) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def make_material(name, colour, roughness=0.6):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*colour, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    # The Workbench engine (and the window's Solid view) do not read
    # the node tree. They use this separate "viewport colour". Set
    # both, or the two engines will disagree about your scene.
    mat.diffuse_color = (*colour, 1.0)
    return mat


# Start from a truly empty scene, not the factory cube scene.
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# A dim blue-grey world behind everything.
world = bpy.data.worlds.new("World")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.07, 0.10, 1.0)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0

# Ground: one big flat plane, mid grey.
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
ground = bpy.context.object
ground.name = "Ground"
ground.data.materials.append(make_material("GroundGrey", (0.45, 0.45, 0.45)))

# A red cube, 2 x 2 x 2, resting on the ground (centre at z = 1).
bpy.ops.mesh.primitive_cube_add(size=2, location=(-1.6, 0, 1))
block = bpy.context.object
block.name = "Block"
block.data.materials.append(make_material("BlockRed", (0.75, 0.06, 0.05)))

# A blue sphere, radius 1, resting on the ground.
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(1.3, 0.2, 1))
ball = bpy.context.object
ball.name = "Ball"
ball.data.materials.append(make_material("BallBlue", (0.05, 0.20, 0.85)))
for polygon in ball.data.polygons:
    polygon.use_smooth = True

# A green cone in front, radius 1, height 2, resting on the ground.
bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location=(0.1, -1.9, 1))
cone = bpy.context.object
cone.name = "Cone"
cone.data.materials.append(make_material("ConeGreen", (0.10, 0.65, 0.20)))

# One sun light, angled like a late afternoon.
bpy.ops.object.light_add(type="SUN", location=(4, -3, 6))
sun = bpy.context.object
sun.name = "Sun"
sun.data.energy = 3.0
sun.rotation_euler = (math.radians(50), math.radians(10), math.radians(30))

# A camera looking at the middle of the group.
bpy.ops.object.camera_add(location=(6.5, -6.5, 4.2))
camera = bpy.context.object
camera.name = "Camera"
camera.data.lens = 50
look_at(camera, (0, 0, 0.7))
scene.camera = camera

# Small, quick output: 480 x 270 PNG.
scene.render.resolution_x = 480
scene.render.resolution_y = 270
scene.render.image_settings.file_format = "PNG"

out = os.path.join(os.getcwd(), "still-life.blend")
bpy.ops.wm.save_as_mainfile(filepath=out)

print("=== build_scene ===")
print("Saved:", out)
for obj in scene.objects:
    loc = tuple(round(v, 2) for v in obj.location)
    print("  %-8s type=%-8s location=%s" % (obj.name, obj.type, loc))
print("=== end ===")
