# Glossary

**Background mode** — Running Blender with `-b`: no window, no
display needed; the mode every script in this guide runs in.

**Base Color** — The main colour input of the Principled BSDF
node; the colour Cycles and EEVEE read. Not the only colour a
material carries — see *viewport colour*.

**`.blend`** — Blender's file format and extension. One file
holds the whole project database: objects, meshes, materials,
lights, cameras and settings.

**`bpy`** — The Python module that is Blender's API. Everything
the window can do, `bpy` can do; every script here is built
from it.

**BVH** — The spatial map (bounding volume hierarchy) Cycles
builds before tracing, so rays can find nearby geometry
quickly. The long "Updating" phase in render logs is largely
its construction.

**Camera** — The object a render is taken through. A scene has
one *active* camera; with none, rendering is an error, not a
default.

**Census** — This guide's word for counting a picture's pixels
by colour, to prove what the picture contains (chapter 7).

**Cycles** — Blender's path-tracing engine: physically based,
runs on CPU or graphics card, the slow and honest one.

**EEVEE** — Blender's real-time engine (`BLENDER_EEVEE_NEXT`):
draws the scene the way games do. Fast on a graphics card;
falls back to slow software rendering without one.

**Engine** — The program-within-the-program that turns a scene
into pixels: Cycles, EEVEE or Workbench.

**Material** — Shared data describing a surface — colour,
roughness, metalness — organised as a tree of nodes. Objects
wear materials; many objects can wear the same one.

**Mesh** — The shape data an object points at: corners, edges,
faces. Separate from the object, and shareable between objects.

**Node** — One box in a material's (or the world's) little
wiring diagram: an operation with inputs and outputs.

**Object** — A thing in a scene with a position: it points at
data (a mesh, a lamp type, a camera) rather than being it.

**Path tracing** — Working out a picture by following sample
paths of light as they bounce. Cycles' method; see *sample*.

**Principled BSDF** — The standard surface node: one set of
inputs (base colour, roughness, metallic, and more) covering
most real materials.

**Render** — The picture an engine produces from a scene
through the active camera; also the act of producing it.

**Sample** — One traced path's contribution to a pixel. More
samples per pixel: cleaner picture, longer wait.

**Scene** — The whole arrangement a `.blend` file describes:
objects, materials, lights, camera, settings.

**View transform** — The conversion that prepares a render's
linear light values for a screen (AgX in this version of
Blender). Why measured pixel colours are not the numbers typed
into materials.

**Viewport colour** — A material's second, plain colour
(`diffuse_color`), read by Workbench and the window's Solid
view and ignored by Cycles and EEVEE. Chapter 8 demonstrates
the disagreement it can cause.

**Workbench** — The preview engine: flat and fast, built for
checking composition while you work.

**World** — The scene's background: the colour (or sky) behind
everything, and a source of ambient light.
