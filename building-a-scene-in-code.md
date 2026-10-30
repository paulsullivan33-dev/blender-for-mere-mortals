# Building a Scene in Code

**Outcome: a Python script builds the guide's still life from
nothing — ground, three shapes, a sun, a camera — saves it as
`still-life.blend`, and a fresh process reopens the file and
reads back exactly what the script put in.**

**Check: the reopening report lists 6 objects and 4 materials,
with base colours (0.75, 0.06, 0.05), (0.05, 0.2, 0.85) and
(0.1, 0.65, 0.2) among them.**

The example scene is a still life a child could draw: a red
block, a blue ball and a green cone standing on a grey floor,
lit by one sun, seen by one camera. Every element is placed by
`blender-lab/build_scene.py`. Building by script feels indirect
next to dragging shapes in a window, and it buys three things
the window cannot: the scene is **repeatable** (run the script,
get the scene), **readable** (the script is a written record of
every decision), and **checkable** (the next section's reopen
test).

## The script, in order

The script starts by refusing the factory scene:

```python
bpy.ops.wm.read_factory_settings(use_empty=True)
```

An empty start matters. Building on top of the factory cube,
light and camera leaves you with their settings as silent
passengers — the 1920 × 1080 resolution and EEVEE default of
chapter 4 — and a scene nobody fully specified.

Then a world, so the background behind the shapes is a chosen
colour (a dim blue-grey) instead of a default:

```python
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.07, 0.10, 1.0)
```

Then the cast, each created by the same operator the window's
*Add* menu runs — `primitive_cube_add` is the Add ▸ Mesh ▸ Cube
button, wearing a script's clothes:

| Object | Kind      | Location        | Material colour      |
|--------|-----------|-----------------|----------------------|
| Ground | plane 30 m | (0, 0, 0)       | grey (0.45, 0.45, 0.45) |
| Block  | cube 2 m   | (−1.6, 0, 1)    | red (0.75, 0.06, 0.05)  |
| Ball   | sphere r 1 | (1.3, 0.2, 1)   | blue (0.05, 0.2, 0.85)  |
| Cone   | cone h 2   | (0.1, −1.9, 1)  | green (0.1, 0.65, 0.2)  |
| Sun    | sun light  | (4, −3, 6)      | energy 3.0           |
| Camera | camera     | (6.5, −6.5, 4.2)| lens 50 mm           |

The shapes' centres sit at z = 1 because each is 2 m tall (or
wide) and rests on the ground at z = 0. The camera is aimed by
the script's `look_at` helper, which points the camera's −Z
axis at the middle of the group — chapter 2's rule, applied.

One detail in the material helper will matter in chapter 8:

```python
mat.diffuse_color = (*colour, 1.0)
```

Every material gets its colour **twice**: once as the node
tree's Base Color, and once as the plain viewport colour. The
script comments say why — the fast engines read the second one.
Hold that thought until the engines disagree.

Finally the script sets the output size to 480 × 270 (small,
because the lab machine is small and the point is the method,
not the poster) and saves.

## The reopen test

```
$ blender -b --python build_scene.py
Info: Saved as "still-life.blend"
=== build_scene ===
Saved: /home/hatch/workspace/blender-labwork/still-life.blend
  Ground   type=MESH     location=(0.0, 0.0, 0.0)
  Block    type=MESH     location=(-1.6, 0.0, 1.0)
  Ball     type=MESH     location=(1.3, 0.2, 1.0)
  Cone     type=MESH     location=(0.1, -1.9, 1.0)
  Sun      type=LIGHT    location=(4.0, -3.0, 6.0)
  Camera   type=CAMERA   location=(6.5, -6.5, 4.2)
=== end ===

$ ls -la still-life.blend
-rw-rw---- 1 root root 550125 ... still-life.blend

$ blender -b still-life.blend --python inspect_scene.py   (fresh process, reopening the file)
...
Objects (6):
  Ground       type=MESH     location=(0.0, 0.0, 0.0)
  ...
Materials (4):
  BallBlue     base colour=(0.05, 0.2, 0.85)
  BlockRed     base colour=(0.75, 0.06, 0.05)
  ConeGreen    base colour=(0.1, 0.65, 0.2)
  GroundGrey   base colour=(0.45, 0.45, 0.45)
```

A second Blender process, which never ran the build script,
opens the 550 KB file and reports the same six objects at the
same places wearing the same four materials, at the new
480 × 270 size. That is what chapter 1 promised: the `.blend`
file *is* the scene, whole and portable. Everything after this
chapter works on that file.

*Transcript: `blender-lab/transcripts/t01-build-and-reopen.txt`.
The full script is `blender-lab/build_scene.py`.*
