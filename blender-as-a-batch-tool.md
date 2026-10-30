# Blender as a Batch Tool

**Outcome: Blender runs as one honest step in a larger
pipeline — driven by scripts and arguments, producing files
other programs check — and you know the one place its success
signal lies, and how to make it tell the truth.**

**Check: a script containing an error, run with
`--python-exit-code 1`, makes the shell report failure. Run
without the flag, the same error reports success. You have
seen both.**

Everything so far has treated Blender as a program a person
runs. Its second life (chapter 1) is as a *component*: a 3D
step inside a build script, a nightly job, a product-photo
pipeline. The pieces are already familiar — background mode,
scripts, arguments after `--` — and this chapter adds the two
things a pipeline needs that a person doesn't: **repeatability**
and an **honest exit code**.

## Repeatability is already proven

Chapter 9's control experiment is the foundation: same scene,
same settings, same Blender — *identical pixels*, run after
run. A batch tool whose output wanders cannot be tested; one
whose output is exact can be regression-tested like any other
program. Keep a known-good render, re-render on every change
(of scene, settings, or Blender version), and compare. The
census and the material-difference count from `check_png.py`
are ready-made assertions.

## The lying exit code

Now the trap, verbatim from the lab. A script with a misspelt
operator — `primitive_cube_asdd` for `primitive_cube_add`:

```
$ blender -b --python-expr "import bpy; bpy.ops.mesh.primitive_cube_asdd(size=2)"
Traceback (most recent call last):
  ...
AttributeError: Calling operator "bpy.ops.mesh.primitive_cube_asdd" error, could not be found

$ echo $?
0
```

The traceback printed. The work did not happen. And the exit
code — the one signal a shell script, a CI job or a Makefile
actually reads — is **0: success**. Blender's reasoning is
defensible (the *application* ran fine; one script inside it
failed) and the outcome for an unattended pipeline is a folder
of missing pictures discovered by a human, later.

The fix is one flag, and it belongs in every unattended
invocation:

```
$ blender -b --python-exit-code 1 --python-expr "import bpy; bpy.ops.mesh.primitive_cube_asdd(size=2)"; echo $?
1
```

With `--python-exit-code 1`, a Python exception stops the run
and Blender exits with the code you chose. Pair it with the
habits from earlier chapters — a step that checks its output
file exists and passes a census before declaring success — and
the pipeline's failure modes shrink to ones that announce
themselves.

Note the asymmetry the lab found: a *file* Blender cannot open
is already honest. A missing `.blend` prints
`Error: Cannot read file "...": No such file or directory` and
exits 1 without being asked. It is specifically *script*
failures that default to silence.

## Driving it from outside

The pattern this guide's own lab used, generalised:

```
blender -b "$scene" --python-exit-code 1 \
        --python render_still.py -- CYCLES 128 "$out"
python3 check_png.py "$out"        # the gate
```

- Pass per-run choices (engine, samples, output path) as
  script arguments after `--`, not by editing the script.
- One scene per invocation. Blender processes are cheap to
  start next to render times, and isolation means one bad
  scene cannot take the batch with it — its exit code names
  it, and the loop moves on or stops, as you choose.
- Treat the render log's `Saved:` line and the output file's
  existence as *claims*, and the census as the *check*. That
  ordering — claim, then verify — is the whole method of this
  guide, and it survives contact with pipelines precisely
  because the verification is mechanical.

What a pipeline still cannot do is judge the picture. It can
prove the scene's colours are present, the change is where it
belongs, and the file is whole. Whether the picture is *good*
remains a person's call — which is an argument for making the
mechanical checks this thorough: they are the part that can
run while nobody is watching.

*Transcript: `blender-lab/transcripts/t07-failures.txt`.*
