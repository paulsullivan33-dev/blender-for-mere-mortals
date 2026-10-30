# Change One Thing

**Outcome: you repaint one object, re-render, and produce a
measured account of what changed — where in the picture, by
how much, and what provably did not change at all.**

**Check: the control comparison reports 0 differing pixels,
and the real comparison's *material* changes sit in one
bounding box on the Ball's side of the frame, with blue gone
from the census.**

This is the experimental method of the whole guide in one
chapter: change one variable, measure, and run a control so
you know your instrument isn't lying. The variable: the Ball's
colour, blue (0.05, 0.2, 0.85) to orange (1.0, 0.45, 0.05). The
instrument is `check_png.py` with *two* files, which adds a
comparison to its census: how many pixels differ at all, how
many differ *materially* (by more than 10 in some channel —
a line drawn between a change and a tremor), and where the
material differences live.

The edit itself is a script, `blender-lab/recolour_ball.py`,
which opens the scene, finds the material, and changes both of
its colours (node and viewport — chapter 8's lesson, applied).
It prints its own work:

```
=== recolour_ball ===
Before: material BallBlue base colour = (0.05, 0.2, 0.85)
After:  material BallOrange base colour = (1.0, 0.45, 0.05)
Saved: /home/hatch/workspace/blender-labwork/still-life-orange.blend
```

It saves under a **new name** rather than overwriting. Both
versions of the scene now exist, so before-and-after renders
can be made at any time, in any order — the comparison does
not depend on anyone's memory of the earlier state.

## The control

First, the experiment's conscience: render the *unchanged*
scene a second time and compare the two renders.

```
$ python3 check_png.py renders/still-cycles.png renders/still-cycles-again.png   (control: same scene twice)
comparison:
  pixels differing at all: 0 of 129600 (0.0%)
  pixels differing by more than 10 in some channel: 0 (0.0%)
```

**Zero.** At the same settings, Cycles on this machine is
bit-for-bit reproducible: same file in, same pixels out, every
time. That is not a small thing. It means any difference found
below is *caused* — by the scene, the settings, or the version
of Blender — and never by the renderer rolling dice. (It also
means a scripted pipeline can use equality itself as a test:
render a known scene, compare against a kept-good picture, and
any drift is a real event. Chapter 11 uses this.)

## The change

```
$ python3 check_png.py renders/still-cycles.png renders/still-cycles-orange.png   (the recoloured Ball)
comparison:
  pixels differing at all: 67012 of 129600 (51.7%)
  pixels differing by more than 10 in some channel: 22085 (17.0%)
  bounding box of the material change: x 152..394, y 60..253
  average colour inside the box, before: (117.8, 121.1, 139.0)
  average colour inside the box, after:  (164.0, 130.7, 99.3)
```

Three findings, in increasing order of interest:

1. **The census flips as predicted.** In the orange render,
   strongly blue pixels are 0.0% (there is no blue left to
   find) and strongly red rises from 15.3% to 27.9% — the red
   Block plus an orange Ball both census as red-dominant.
2. **The material change is where the Ball is.** The bounding
   box covers the right-hand portion of the frame — x from 152
   to 394 of 480, y from 60 to 253 of 270 — which is the Ball
   and the floor it lights, on the right of the composition.
   The average colour inside the box swings from blue-leaning
   (139.0 in the blue channel against 117.8 red) to
   orange-leaning (164.0 red against 99.3 blue). The change
   landed where the edit was made.
3. **Half the picture differs — slightly.** 51.7% of pixels
   differ at all, though only 17.0% differ materially. The
   control says this is not noise. It is *light transport*: in
   Cycles, the Ball is not only seen, it is a light source one
   bounce removed — its colour tints the light it reflects
   onto the floor and its neighbours. Blue ball, faintly blue
   bounce; orange ball, faintly orange bounce, across half the
   frame at strengths below the material threshold. One
   object's colour leaks into the whole picture, a little.
   That is the physical honesty you pay Cycles' render time
   for, made visible by counting.

## The habit

Specify the change as a script. Save to a new name. Render
before and after with identical settings. Compare against a
control that proves the instrument steady. Report the census,
the box, and the size of the change — not "it looks different".
Everything in chapters 10 and 11 is this habit, automated.

*Transcript: `blender-lab/transcripts/t06-change-one-thing.txt`.*
