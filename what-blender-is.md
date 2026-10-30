# What Blender Is

**Outcome: you can say what Blender takes in, what it gives back,
and why this guide spends so much time outside its window.**

**Check: name the four things every render needs — a scene, a
camera, a light, and an engine — before you finish the chapter.**

Blender is a program for making 3D pictures and films. Studios
use it for animation, hobbyists for models and prints, and it
costs nothing and runs on Linux, Windows and macOS. Underneath
all of that, its job is simple to state:

- **In:** a *scene* — a description of shapes, what they are
  made of, where the lights are, and where a camera sits.
- **Out:** a *picture* (or a film) — the scene as that camera
  would see it, worked out by a rendering *engine*.

The scene lives in a file with the extension `.blend`. The file
is not just the shapes: it is a little database holding the
geometry, the materials, the lights, the camera, and the
settings, all together. Open the file and everything needed to
reproduce the picture is there. Chapter 5 proves this by
building a scene, saving it, and reading it back in a fresh
process that knows nothing except what the file tells it.

## The window, and the life behind it

Most people meet Blender through its window: a 3D view you can
orbit, panels of settings, a timeline. That window is real
work, and this guide describes it where it matters. But the
window is only one front door. The same application also runs
like this:

```
blender -b still-life.blend --python render_still.py
```

The `-b` is *background mode*: no window, no mouse, just the
scene, a Python script, and whatever the script produces. Every
button in the window corresponds to an operation the script can
call — the window is, in a fairly literal sense, a remote
control for the same machinery. The scripting language is
Python, and Blender ships with its own Python built in.

This guide leans on the scripted door for a practical reason:
**it can be checked**. A person at a window can see whether a
render looks right. A script on a machine with no display
cannot see anything — so it has to *measure*, and measurements
can be written down, repeated, and argued with. Chapter 7
measures a render's pixels and finds, in them, each colour the
scene was built from. Chapter 9 changes one colour and measures
exactly which pixels moved, with a control experiment to prove
the rest stayed still. That discipline — don't trust the file,
measure it — is worth learning even if you always work at a
window on a fast machine.

## What Blender is not

Blender is not a CAD program in the engineering sense: it
describes surfaces, not tolerances, and chapter 12 returns to
the difference. It is not a game engine, though games borrow
its models. And it is not one tool: modelling, sculpting,
animation, video editing and more share the `.blend` format.
This guide covers one honest slice — still pictures of scenes,
built and rendered — and labels everything beyond that slice
as documented-only, in the chapters and in `criteria.md`.

## The shape of the rest of the guide

Chapter 2 takes the scene apart into its moving parts.
Chapter 3 installs Blender and proves the install. Chapters 4
to 6 read a scene, build one, and render it. Chapters 7 to 10
are the verification half: proving pictures, comparing engines,
changing one thing at a time, and running Blender as a batch
tool that other programs can drive.
