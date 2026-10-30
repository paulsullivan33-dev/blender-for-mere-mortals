# Proving the Picture

**Outcome: instead of trusting that the render worked, you
measure the PNG and find the scene inside it — the ground, and
each of the three colours you built in, present in roughly the
shares the composition predicts.**

**Check: a healthy render of the still life reports thousands
of distinct colours and finds all three strong colours. Zero
strong colours, or a few dozen distinct colours in total, means
the picture is not your scene.**

The lab could not see its render. Neither can a render farm at
3 a.m., a CI job, or a script deciding whether to go on to the
next step. So the guide's habit, from here on, is: **every
render gets measured**. The instrument is
`blender-lab/check_png.py`, an ordinary Python script (run with
the system Python, not Blender's) that opens a PNG with the
Pillow library and reports:

- the dimensions, counted from the file, not from memory;
- how many *distinct* colours the picture uses;
- the five commonest colours, with their shares;
- a census of *strongly coloured* pixels — pixels where one
  channel (red, green or blue) beats the other two by 40 or
  more — which is a plain-language way of asking "how much of
  this picture is plainly red, plainly green, plainly blue?"

## The still life, measured

```
$ python3 check_png.py renders/still-cycles.png
renders/still-cycles.png
  size: 480 x 270 (129600 pixels)
  distinct colours: 6940
  five commonest colours (RGB, count, share):
    (141, 143, 145)    8860    6.8%
    (140, 143, 145)    5926    4.6%
    ...
  strongly coloured pixels (one channel ahead by 40+):
    red     19817   15.3%
    green   13696   10.6%
    blue    17349   13.4%
```

Read the evidence the way you'd read any measurement:

- **The size is the size you ordered** — 480 × 270, 129,600
  pixels. A render that silently fell back to some other
  resolution fails here first.
- **6,940 distinct colours** is what a lit, shaded scene looks
  like as a number. A flat or blank render uses a handful. The
  thousands come from light falling off across surfaces, soft
  shadow edges, and the grain of a 32-sample render — every
  slightly different pixel is a slightly different colour.
- **The commonest colour is the ground.** (141, 143, 145) — a
  neutral grey a touch brighter than the material's 0.45 —
  covers most of the top five rows between them. That is the
  grey floor under a strong sun, filling the bottom of the
  frame. It is *not* the number typed into the material
  (0.45, 0.45, 0.45): the picture's colours are the material's
  colours after lighting and after Blender's view transform
  prepares them for a screen. Chapter 12 returns to this: you
  measure the picture, not the recipe.
- **All three built-in colours are found**, in shares that fit
  the composition: the red Block 15.3%, the blue Ball 13.4%,
  the green Cone 10.6% (the Cone stands in front but is the
  narrowest of the three). Nobody told the script where to
  look. If an object were missing, misplaced behind the
  camera, or painted the wrong colour, its share collapses —
  and chapter 9 uses exactly that collapse as a detector.

## What this does not prove

A census proves presence, not beauty, and not exact position:
a red smear anywhere would count as red. Where position
matters, chapter 9's method — compare two pictures and find
*where* they differ — is the stronger instrument. And a census
can be fooled by a coincidence of colours; it is a gate, not a
verdict. But as a gate it is exactly what a pipeline needs:
cheap, automatic, and very hard for a broken render to pass
by accident.

*Transcript: `blender-lab/transcripts/t03-proving-the-picture.txt`.*
