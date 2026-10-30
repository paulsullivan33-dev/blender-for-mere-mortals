# Reading a Scene

**Outcome: you can open any `.blend` file — starting with the
one Blender itself opens with — and get a plain report of what
is in it, without the window and without guessing.**

**Check: the report on the factory scene names three objects.
If yours names more, you are not looking at the factory scene.**

Before building anything, learn to *read*. Blender's own
starting point is the factory scene, the thing behind every
fresh window: one cube, one light, one camera. Here it is,
read by the lab's inspection script instead of by eye:

```
$ blender -b --python inspect_scene.py   (factory default scene)
=== inspect_scene ===
Blender version: 4.5.9 LTS
Scene name: Scene
Render engine: BLENDER_EEVEE_NEXT
Resolution: 1920 x 1080
Camera: Camera

Objects (3):
  Cube         type=MESH     location=(0.0, 0.0, 0.0)
  Light        type=LIGHT    location=(4.08, 1.01, 5.9)
  Camera       type=CAMERA   location=(7.36, -6.93, 4.96)

Materials (2):
  Dots Stroke  base colour=None
  Material     base colour=(0.8, 0.8, 0.8)
=== end ===
```

## What the report is telling you

Read it against chapter 2's moving parts:

- **Three objects, three jobs.** `Cube` is the shape (type
  MESH), sitting at the origin. `Light` is a lamp (type LIGHT)
  up and to one side. `Camera` is the view (type CAMERA) —
  the scene's active camera, named on the `Camera:` line.
- **The house defaults are visible.** The engine is EEVEE
  (`BLENDER_EEVEE_NEXT`) and the picture size is 1920 × 1080:
  Blender's factory opinion of a render. Nothing about those
  is a law; both are settings in the file, and later chapters
  change both and show the change sticking.
- **The cube's material is a plain grey.** `Material` has base
  colour (0.8, 0.8, 0.8) — a light neutral grey, which is why
  the famous default cube is grey. (`Dots Stroke`, with no base
  colour, is a leftover material for the grease-pencil drawing
  tools; it belongs to no object. Files accumulate such
  passengers. The report shows the file as it is, passengers
  and all.)

## The instrument

The script is `blender-lab/inspect_scene.py`, and it is short
enough to keep by heart. It walks `bpy.context.scene.objects`,
prints each object's name, type and location, then walks
`bpy.data.materials` and reports each material's Principled
BSDF base colour. It is the pattern for nearly everything in
this guide: **ask the data, print the answer**. Whenever a
later chapter claims a scene contains something, a script like
this one is what checked.

Two ways to run it, both used in this guide:

- `blender -b --python inspect_scene.py` — no file named, so
  Blender starts from the factory scene.
- `blender -b somefile.blend --python inspect_scene.py` — the
  file is loaded first, then the script runs against it.

That second form, pointed at a file you did not build, is the
single most useful Blender habit this guide teaches. Run it on
any `.blend` you are handed — a tutorial's, a colleague's, one
of your own from two years ago — before you render or edit
anything. The scene will introduce itself.

*Transcript: `blender-lab/transcripts/t00-version-and-default-scene.txt`.*
