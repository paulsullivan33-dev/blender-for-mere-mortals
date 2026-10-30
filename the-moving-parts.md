# The Moving Parts

**Outcome: given any Blender scene, you can say which part
holds the shape, which holds the colour, which holds the
light, and which one decides what the picture shows.**

**Check: run the inspection from chapter 4 on the factory scene
and point at the line that is the shape, the line that is the
light, and the line that is the camera.**

A scene has five kinds of part. Keeping them separate in your
head is most of Blender literacy, because nearly every surprise
in Blender is one part being mistaken for another.

## Objects: the things in the scene

An *object* is a thing with a position: a location, a rotation,
a size. The factory scene has three — a cube, a light, a
camera (chapter 4 reads them out). The guide's example scene
has six: a ground plane, a block, a ball, a cone, a sun and a
camera.

An object is mostly a coat-hanger. The actual shape hangs on
separate *mesh data* — the list of corners, edges and faces —
which the object points at. Two objects can point at the same
mesh and show the same shape in two places. Moving an object
moves the hanger; editing the mesh changes the shape for every
object wearing it. In scripts, the object is `bpy.data.objects`
and the mesh is `bpy.data.meshes`; chapters that touch both
say which they mean.

Blender's world is measured in metres by default, and up is
the **Z** axis (unlike many games, where up is Y). A location
like `(1.3, 0.2, 1.0)` is 1.3 m along X, 0.2 m along Y, and
1.0 m up. The example ball has radius 1 m and sits with its
centre at z = 1.0, so its bottom just touches the ground at
z = 0 — arithmetic the build script in chapter 5 does out loud.

## Materials: what a surface is made of

A *material* describes a surface: its colour, whether it is
rough or glossy, metal or not. In modern Blender a material is
a small tree of *nodes* — little boxes wired together — and the
node that matters first is the **Principled BSDF**, the standard
surface. Its *Base Color* input is the colour you mean when you
say "the red cube".

Two facts about materials cause real confusion, and both are
demonstrated in this guide:

- A material is shared data, like a mesh. Paint the material
  and every object wearing it changes. Chapter 9 recolours one
  material and exactly one object changes colour — because only
  one object wears it.
- A material quietly carries a **second colour**: a plain
  "viewport colour" used by the fast preview engine and the
  window's Solid view, separate from the node tree. Set one and
  not the other and the engines will disagree about your scene.
  Chapter 8 demonstrates this with a ball that is blue to one
  engine and grey to another.

## Lights: why anything is visible

A render with no light is a black rectangle. Lights are
objects too — they have positions — but their data is a lamp
type (point, spot, sun, area) and a strength. A **sun** light
is special: only its direction matters, not its position,
because it stands in for a light infinitely far away. The
example scene uses one sun, angled like a late afternoon.

There is also light that comes from the *world* itself — a
background glow behind everything. The build script sets the
world to a dim blue-grey, which is what fills the corners of
the picture that no object covers.

## The camera: the only view that renders

A scene can hold several cameras, but exactly one is the
*active* camera, and a render is the scene from that camera's
position, through its lens. No camera, no render — chapter 13
has the error message verbatim (`Error: Cannot render, no
camera`) and the empty space where the file would have been.

A camera aims with its local axes: it looks down its own **−Z**.
Scripts aim it by pointing that axis at a target, which is what
the `look_at` helper in the build script does.

## The engine: who works out the picture

Last, the *engine* — the program-within-the-program that turns
scene into pixels. Blender ships three:

- **Cycles** traces the paths light takes, bouncing them
  around the scene. Slow, physically honest, runs on CPU or
  graphics card.
- **EEVEE** draws the scene the way games do, in one pass per
  object. Fast on a graphics card, approximate in ways that
  usually don't matter.
- **Workbench** is the preview engine: flat, quick, and the
  one that reads the second colour mentioned above.

Same scene, three engines, three pictures that agree in
outline and differ in detail. Chapter 8 renders all three and
counts the differences rather than asserting them.
