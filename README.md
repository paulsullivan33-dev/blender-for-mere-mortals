# Blender for Mere Mortals

Most 3D pictures are made inside a window:
you push shapes around with a mouse, and
sooner or later you press Render and a
picture comes out. **Blender** does that —
it is the free program behind a large
share of the world's independent 3D art,
animation and film work. But Blender has
a second life that the window hides. The
whole application is scriptable in Python,
and it runs happily with no window at all.
A scene can be built by a program, rendered
by a program, and checked by a program.
That second life is what this guide is
mostly about, because it can be *proved*:
every claim here is backed by a transcript
of a real run.

This guide explains how Blender thinks
about a scene — objects, materials, lights,
a camera — how to install it, how to read
a scene you did not build, and how to build
one from code. Then it renders the same
small scene three ways, with the three
engines Blender ships, and does something
most 3D guides skip: it **proves the
picture is real**. The lab that wrote this
guide had no display. It could not look at
a single render it made. So every claim is
checked by measurement instead: the file's
size, its dimensions, its colours counted
pixel by pixel, and a control experiment
that renders the same scene twice to show
the output does not drift. That turns out
to be a good habit for anyone, display or
not, because a renderer that fails quietly
still writes a file — sometimes a blank one.

The lab behind this guide ran the real
thing: **Blender 4.5.9 LTS**, the official
Linux release archive, in background mode
on a small machine with no graphics card.
Against its example scene — a red block, a
blue ball and a green cone on a grey floor,
lit by one sun — the lab built the scene
twice over from a script, reopened the saved
file in a fresh process to prove the file
holds the scene, rendered it with Cycles,
with Workbench and with EEVEE, recoloured
one object and measured exactly which
pixels moved, and deliberately broke
things: a misspelt command that reports
success anyway, a render with no camera,
and a file that does not exist.

What the lab could not do, it did not
fake. It had no display and no graphics
card, so the window itself — modelling by
hand, sculpting, dragging lights around —
is taught from Blender's documentation and
labelled as such wherever it appears.
EEVEE, the engine built for a graphics
card, fell back to software rendering on
the lab machine and was *slower* than the
CPU engine there; on a machine with a real
graphics card that order reverses, and the
guide says so rather than letting the lab's
timings pose as the tool's character.
`criteria.md` keeps the full ledger of what
was run and what was only read.

## What this guide covers

- [**What Blender is**](what-blender-is.md) —
  the mental model: a scene in a file, a
  camera, an engine, a picture out — and
  the second, scriptable life behind the
  window
- [**The moving parts**](the-moving-parts.md) —
  objects and the data they hold, materials
  as little node trees, lights, the camera,
  and which part holds what
- [**Installing Blender**](installing-blender.md) —
  the release archive, the checksum that
  proves the download, and the version
  check that proves it runs
- [**Reading a scene**](reading-a-scene.md) —
  opening the factory scene — a cube, a
  light, a camera — and having a script
  report what is in it
- [**Building a scene in code**](building-a-scene-in-code.md) —
  a still life of simple shapes built by a
  Python script, saved to a `.blend` file,
  and reopened in a fresh process to prove
  the file holds it all
- [**Your first render**](your-first-render.md) —
  one command, one PNG: the Cycles engine
  turning the scene into a picture, and
  what its progress log is telling you
- [**Proving the picture**](proving-the-picture.md) —
  how to know a render really contains
  your scene: dimensions, thousands of
  distinct colours, and a census that finds
  the red, the green and the blue you put in
- [**Three engines, one scene**](three-engines.md) —
  Cycles, EEVEE and Workbench rendering the
  same scene; where they agree, where they
  differ, and the second colour every
  material quietly carries
- [**Change one thing**](change-one-thing.md) —
  repaint one object, render again, and
  measure which pixels moved — with a
  control render proving the rest of the
  picture does not drift on its own
- [**Blender as a batch tool**](blender-as-a-batch-tool.md) —
  scripts, arguments after the `--`,
  rendering farms of one, and the exit
  code that lies to you unless you ask
  for the honest one
- [**Recipes**](recipes.md) — render every
  file in a folder, render one scene every
  way it can be rendered, make colour
  variants, and gate a pipeline on a
  picture census
- [**The neighbours**](the-neighbours.md) —
  OpenSCAD's code-only solids, the 3D
  printing pipeline, parametric CAD, and
  the commercial studios: what each does
  that Blender doesn't, and vice versa
- [**Limits**](limits.md) — stills only in
  this guide, a CPU that renders slowly at
  production sizes, an API that changes
  between versions, a binary file format
  git cannot read, and pictures whose
  measured colours are not the numbers
  you typed in
- [**Troubleshooting**](troubleshooting.md) —
  the script error that exits 0, the
  render with no camera, the file that
  cannot be read, the grey object in
  Workbench, and the EGL errors on a
  machine with no display
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Animation, rigging, sculpting, video
editing and the rest of Blender's very
large surface — Blender is several
professional tools sharing one file
format, and this guide covers the still
picture: scenes, materials, lights and
renders. Modelling by hand in the window
is described so a reader can follow it,
but it is not lab-verified here; the
verified path is the scripted one, and
chapter 12 is honest about the boundary.
Rendering other people's scenes at
production size, and render farms bigger
than one machine, are pointed at, not
taught.

## How to use this guide

Read chapter 1 for the model, and
chapter 2 before installing anything —
knowing which part holds what turns
later confusion into a named problem.
Chapters 3 and 4 get you a program and a
first look inside a scene; chapters 5
and 6 build a scene and render it in the
same sitting. Chapter 7 is the one to
read slowly even if you have a display:
its checks are how you catch the silent
failures — including the script error
that reports success — before they reach
anything that depends on the picture.
The lab's transcripts live in
`blender-lab/transcripts/`; its scripts
are `blender-lab/build_scene.py`,
`blender-lab/inspect_scene.py`,
`blender-lab/render_still.py`,
`blender-lab/recolour_ball.py` and
`blender-lab/check_png.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [3D Printing for Mere Mortals](https://paulsullivan33-dev.github.io/3d-printing-for-mere-mortals/)
- [OpenSCAD for Mere Mortals](https://paulsullivan33-dev.github.io/openscad-for-mere-mortals/)
- [Python for Mere Mortals](https://paulsullivan33-dev.github.io/python-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/blender-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/blender-for-mere-mortals/blob/main/LICENSE-CODE).
