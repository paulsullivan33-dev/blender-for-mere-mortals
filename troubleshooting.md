# Troubleshooting

**Outcome: the failures this guide's lab actually hit, each
with its verbatim evidence, its cause, and its fix.**

**Check: every entry can be reproduced from its transcript —
if your failure matches none of them, it is a new entry, not
a variant.**

## The script failed and the shell said success

*Evidence (t07).* A traceback in the output —

```
AttributeError: Calling operator "bpy.ops.mesh.primitive_cube_asdd" error, could not be found
```

— followed by an exit code of 0.

*Cause.* Blender reports a Python exception but considers its
own run successful. Any caller reading only the exit code
(a shell, CI, a Makefile) is told the work happened.

*Fix.* Always run unattended Blender with
`--python-exit-code 1`. The same failure then exits 1. Chapter
10 has both runs in full. And gate on the output file's
existence and census as well — an exit code is a claim, not
the check.

## Cannot render, no camera

*Evidence (t07).*

```
RuntimeError: Error: Cannot render, no camera
```

and no output file at all.

*Cause.* The scene has no active camera — deleted, never
added, or `scene.camera` unset by a script. A render *is* the
camera's view, so there is nothing to fall back to.

*Fix.* Inspect the scene before rendering (chapter 4's script
prints `Camera: NONE` in this case), and make build scripts
set `scene.camera` explicitly, as `build_scene.py` does.

## The file cannot be read — and this one is honest

*Evidence (t07).*

```
Error: Cannot read file "/home/hatch/workspace/blender-labwork/no-such-file.blend": No such file or directory
```

Exit code 1, unasked.

*Cause.* The path is wrong, or the file is not a `.blend` at
all (a classic: an error page saved under a `.blend` name —
chapter 3's size check catches the same disease one step
earlier).

*Fix.* Check the path and the file's size before debugging
anything downstream. Note the asymmetry with the first entry:
file errors are fatal, script errors are not, until you make
them so.

## The object is the wrong colour — but only sometimes

*Evidence (t04).* Workbench shows the object grey while Cycles
shows it coloured (or the reverse after an edit).

*Cause.* Two colour fields, two readers (chapter 8): the node
tree's Base Color feeds Cycles and EEVEE; the viewport colour
(`diffuse_color`) feeds Workbench and the window's Solid view.
One was set; the other still holds a default.

*Fix.* Set both, in the material's creation code — as
`build_scene.py` does — or in the window: the material's
*Viewport Display* colour beside its node colour.

## EGL errors on a headless machine

*Evidence (t05).*

```
EGL Error (0x3009): EGL_BAD_MATCH: Arguments are inconsistent ...
```

*Cause.* EEVEE asked for a hardware graphics surface and the
machine has none. Blender retries, then falls back to software
rendering and completes — slowly.

*Fix.* Nothing is broken; choose knowingly. On a headless box,
prefer Cycles on CPU for scripts, or launch through the
`blender-softwaregl` wrapper shipped in the archive to make
the software path explicit. Do not quote the resulting EEVEE
timings as EEVEE's character (chapter 12).

## The render is far slower than the guide's numbers

*Evidence: the whole lab.* The same render took 12 seconds
and 23 seconds at different hours.

*Cause.* Usually settings, not mystery: resolution multiplies
pixels (1920 × 1080 is sixteen times 480 × 270), Cycles'
sample count multiplies tracing, and a shared or busy machine
divides everything. The render log's sample lines show the
rate; the estimate after sample 1 is pessimistic and
converges, so judge by sample 10, not sample 1.

*Fix.* Compose at Workbench speed, test-render at small size
and low samples, and only then pay for the full picture —
the workflow chapters 6 to 8 are arranged in that order on
purpose.
