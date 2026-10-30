# Recipes

**Outcome: four jobs people actually hand to a scripted
Blender, each assembled only from parts the earlier chapters
ran and measured — no new machinery, no unverified steps.**

Each recipe names the chapters it recombines. Timings are the
lab's small machine; yours will differ.

## 1. Render every scene in a folder

*From chapters 6 and 10.* A folder of `.blend` files becomes a
folder of pictures, one honest failure not stopping the rest:

```bash
for scene in scenes/*.blend; do
    name=$(basename "$scene" .blend)
    blender -b "$scene" --python-exit-code 1 \
            --python render_still.py -- CYCLES 128 "renders/$name.png" \
        || echo "FAILED: $scene"
done
```

The `--python-exit-code 1` is doing the recipe's real work:
without it, the `||` never fires and the loop reports a clean
sweep over a folder of gaps.

## 2. One scene, every engine, for comparison

*From chapter 8.* When a scene will be worked on interactively
but delivered from Cycles, render all three up front and
compare the censuses before anyone falls in love with a
preview:

```bash
for engine in BLENDER_WORKBENCH BLENDER_EEVEE_NEXT CYCLES; do
    blender -b scene.blend --python render_still.py -- $engine 64 "check-$engine.png"
    python3 check_png.py "check-$engine.png"
done
```

If Workbench's census is missing a colour the others have,
you have met chapter 8's second colour — fix the viewport
colour in the scene, not in the comparison.

## 3. Colour variants of one product shot

*From chapter 9.* A script that loads the scene, sets one
material's two colours, saves under a new name and renders —
run once per colour on a list. `recolour_ball.py` is the
one-colour instance; the generalisation is a loop over
(name, colour) pairs, each producing `scene-<name>.blend` and
its render. Keep every variant's file: variants you can
re-render are worth more than pictures you cannot reproduce.

Verify each variant the chapter 9 way — its census should show
the old colour gone (or shrunk to whatever else shares it) and
the new colour present at the object's expected share.

## 4. A render gate for a pipeline

*From chapters 7, 9 and 10.* Before a nightly job publishes
its pictures, it proves them:

1. Render with `--python-exit-code 1`; a non-zero exit stops
   the job.
2. Check the file exists and is not absurdly small.
3. Run `check_png.py` and require the expected strong colours
   to be present at roughly their expected shares.
4. If a known-good render exists, compare: a material
   difference where none was scheduled is a change to be
   explained, not shipped.

None of the four steps judges whether the picture is good.
All four together make it very hard for a *broken* picture —
blank, colourless, half a scene, last week's scene — to reach
an audience unnoticed, which is the failure that actually
happens to unattended rendering.
