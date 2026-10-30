# Limits

**Outcome: you can name what this guide did not do, what
Blender itself makes slow or awkward, and which numbers in the
earlier chapters belong to the lab machine rather than to
Blender.**

**Check: for each timing quoted in the guide, you can say
which machine earned it.**

## The guide's limits

- **Stills only.** Animation, rigging, sculpting, simulation,
  compositing and video editing are most of Blender by volume.
  None is covered here, and none was run in the lab. The
  methods transfer (a frame is a frame); the specifics don't.
- **The window is documented, not verified.** The lab had no
  display, so every claim about working interactively —
  modelling by dragging, sculpting, the node editor's feel —
  comes from Blender's documentation. The verified surface is
  background mode and the Python API underneath the window.
- **One scene, small.** The example is four shapes and a sun
  at 480 × 270. Real scenes stress everything this guide found
  easy: memory, render time, file size, organisation. The
  *method* — build from code, reopen to verify, census the
  render, change one thing — is the part claimed to scale.

## Blender's own edges, as the lab met them

- **CPU rendering is slow at honest settings.** 32 samples at
  480 × 270 took seconds; multiply the pixels by sixteen for
  1920 × 1080 and the samples by four or more for a clean
  final, and a CPU render of a rich scene is an overnight job.
  Graphics cards exist in this story as the answer, and the lab
  didn't have one.
- **EEVEE needs a graphics stack.** On the display-less lab
  machine it fell back to software and took two minutes for a
  trivial scene (chapter 8). That is a deployment limit, not a
  defect — but a headless render server is exactly where you
  would meet it, so meet it here first.
- **Script failures default to a success exit code.** Chapter
  10's trap is a limit of the tool's defaults: pipelines must
  opt into honesty with `--python-exit-code`.
- **The API moves.** Blender's Python follows the application,
  and the application changes: engine names, operator
  signatures and node layouts differ across major versions
  (this guide's `BLENDER_EEVEE_NEXT` is itself a renamed
  thing). Scripts written for 4.5 may need edits for 5.x; the
  transcripts are therefore labelled with the version that
  produced them, and the version check in chapter 3 is the
  first step of debugging any script from the internet —
  including this guide's, in a few years.
- **`.blend` is binary.** Git can store it but cannot diff or
  merge it; two people editing one scene cannot combine their
  work the way programmers combine code. The mitigations are
  social (one editor at a time) and structural (build scenes
  from scripts, which *are* text — chapter 5's method again).
- **Measured colours are not typed colours.** A render's
  pixels pass through lighting and a view transform on their
  way to the file. The census measures the picture honestly,
  but recovering "the material was (0.05, 0.2, 0.85)" from pixel
  values is not possible and not the census's job.

## Numbers that belong to the lab

Timings (Cycles ≈12–23 s, Workbench ≈1 s, EEVEE ≈2 min) were
earned on a shared 2-CPU sandbox with no graphics card, under
other tenants' load, and are quoted as ranges for that reason.
The censuses, the zero-difference control, the bounding box
and the exit codes are properties of the scene and the
software, and should reproduce anywhere. Knowing which kind of
number you are holding is most of reading benchmarks.
