# Your First Render

**Outcome: the still life becomes a PNG — 480 × 270, rendered
by Cycles on the CPU — and you can read the renderer's log well
enough to know it worked.**

**Check: the transcript ends with `Saved:` naming your file,
a total time, and a PNG on disk of roughly 150 KB. A file of a
few hundred bytes is a failure wearing a success's clothes
(chapter 7 takes that test further).**

A render needs a scene, an engine and an output path. The lab's
render script, `blender-lab/render_still.py`, takes all three
from the command line — everything after the `--` belongs to
the script, which is Blender's convention for passing arguments
past its own options:

```
$ blender -b still-life.blend --python render_still.py -- CYCLES 32 renders/still-cycles.png
```

Read it left to right: background mode; load `still-life.blend`;
run the script; the script's arguments are engine `CYCLES`,
32 *samples*, and the output file. The script sets the engine,
sets Cycles to use the CPU, and calls the same render operator
the window's Render button calls.

## Samples, briefly

Cycles works out the picture by tracing sample paths of light
— thousands of them per pixel would be ideal, and the sample
count is the dial between *fast and grainy* and *slow and
clean*. 32 is low: a learning number, chosen so the lab's small
machine finishes in seconds. Chapter 12 is honest about what
production numbers look like. The picture at 32 samples is
slightly grainy, and chapter 7's counting method is built to
see the scene through that grain rather than pretend it away.

## Reading the log

Cycles narrates as it goes. Trimmed to the lines that matter:

```
Fra:1 Mem:8.83M (Peak 9.10M) | Time:00:00.23 | ... | Updating Lights | Computing tree
Fra:1 Mem:18.25M (Peak 18.25M) | Time:00:01.29 | Remaining:00:32.89 | ... | Sample 1/32
Fra:1 Mem:22.21M (Peak 28.14M) | Time:00:15.24 | ... | Sample 32/32
Fra:1 Mem:22.21M (Peak 28.14M) | Time:00:15.24 | ... | Finished
Saved: '/home/hatch/workspace/blender-labwork/renders/still-cycles.png'
Time: 00:15.36 (Saving: 00:00.12)
```

- `Fra:1` — frame 1. Animation renders count up; a still is a
  one-frame film.
- The long *Updating* phase is Cycles preparing the scene —
  building its map of the geometry (the BVH), placing the
  lights. For a big scene this phase alone can take minutes;
  for this one it is a blink.
- `Sample 1/32` … `Sample 32/32` — the actual tracing, with a
  running memory figure and an estimated remainder that starts
  pessimistic (`Remaining:00:32.89`) and converges. On the
  lab's shared two-CPU machine, whole renders of this scene
  took between about 12 and 23 seconds across the day's runs —
  the guide quotes ranges because a shared machine's timings
  are weather, not specifications.
- `Saved:` and the total `Time:` are the success lines. Their
  absence is the failure signal; chapter 13 shows runs that end
  without them.

The result is a 150,200-byte PNG. Size alone does not prove a
picture — a file can be large and wrong — but it is the first
gate: renders that failed quietly in the lab's other guides
usually announced themselves as absurdly small files. The next
chapter opens the file and counts what is inside it.

*Transcript: `blender-lab/transcripts/t02-first-render-cycles.txt`.*
