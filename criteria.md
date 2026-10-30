# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's scene is an invented still life of simple shapes.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool and
   the guide cannot do: stills only here, CPU rendering slow at
   production size, EEVEE needing a graphics stack, an API that
   changes between versions, a binary file format, and measured
   colours that are not the typed colours.
8. **The ethics rule is in the text, early.** Blender raises no
   interception question of the kind other guides in this
   series carry; its own line is drawn in chapter 1 instead —
   renders in this guide are made from scenes the lab built
   itself, and the measurement method exists so that claims
   about a picture never rest on an author's say-so.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, shared Ubuntu sandbox with no
display and no graphics card, shared with other work while the
lab ran (timings are therefore ranges, and the guide says so).
Blender **4.5.9 LTS** was installed from the official release
archive `blender-4.5.9-linux-x64.tar.xz` (377,929,956 bytes,
SHA-256
`dcdc3eca6c9825bb35a8033b689c053f3cb5a9b0cd2a61b2eac2a49436b4ad3d`,
computed in the lab; readers verify against the release page,
as chapter 3 instructs) and run unmodified, in background mode
only. All transcripts live in `blender-lab/transcripts/`; the
scripts are `blender-lab/build_scene.py`,
`blender-lab/inspect_scene.py`, `blender-lab/render_still.py`,
`blender-lab/recolour_ball.py` and `blender-lab/check_png.py`
(the last runs under the system Python with Pillow, not under
Blender).

The lab had **no display and no way to look at a render**.
Every claim about a picture is therefore a measurement —
dimensions, file size, distinct-colour counts, strong-colour
censuses, and pixel-by-pixel comparisons — and the guide never
grades how a render *looks* beyond what those measurements
support.

Run for real, with transcripts as evidence:

- Version and build facts for 4.5.9 LTS, the archive's size and
  checksum, and a scripted read of the factory scene: 3 objects
  (Cube, Light, Camera), engine EEVEE, 1920 × 1080, default
  material base colour (0.8, 0.8, 0.8) (t00).
- The still life built from code (6 objects, 4 materials),
  saved as a 550,125-byte `.blend`, and reopened in a fresh
  Blender process that reported the same objects, locations,
  materials, colours and resolution from the file alone (t01).
- A Cycles render on CPU, 480 × 270 at 32 samples: whole runs
  of about 12–23 s on the shared machine, a 150,200-byte PNG,
  and the render log's Saved/Time lines (t02).
- The pixel census of that render: 6,940 distinct colours;
  strongly red pixels 15.3%, green 10.6%, blue 13.4%, matching
  the three objects built into the scene; the ground grey the
  commonest colour (t03).
- Workbench rendering the same scene (≈1 s) with a census in
  family (5,168 distinct colours; 15.2 / 8.5 / 12.1); and the
  viewport-colour experiment: resetting one material's
  `diffuse_color` to grey drove Workbench's blue share to
  exactly 0.0% with red and green unchanged to the pixel,
  while the same change under Cycles left the census identical
  — the two engines read different colour fields (t04).
- EEVEE on the display-less machine: three verbatim EGL errors,
  a software-rendering fallback, a completed 64-sample render
  in 2 minutes 2 seconds, exit code 0, and a census in family
  (3,557 distinct colours; 15.3 / 11.6 / 13.3) (t05).
- Change-one-thing, with a control: rendering the unchanged
  scene twice produced **zero** differing pixels, while the
  recoloured Ball (blue to orange) changed 51.7% of pixels at
  all and 17.0% materially, with the material changes bounded
  at x 152..394, y 60..253 and the box's average colour moving
  from blue-leaning (117.8, 121.1, 139.0) to orange-leaning
  (164.0, 130.7, 99.3); the orange census shows blue at 0.0%
  and red at 27.9% (t06).
- Failures: a misspelt operator's traceback with exit code 0,
  and exit code 1 for the same error under
  `--python-exit-code 1`; a render with no camera failing with
  `Error: Cannot render, no camera` and writing no file; a
  missing `.blend` failing with `Error: Cannot read file` and
  exit code 1 (t07).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Everything in the window: interactive modelling, sculpting,
  the node editor, the timeline, and Solid/Material Preview
  views as experiences. (Workbench *renders* were run; the
  window they normally appear in was not.)
- Animation of every kind, rigging, simulation, compositing,
  and the video sequencer; the example pipeline here renders
  frame 1 of a scene as a still.
- Cycles on a graphics card, and EEVEE at its proper speed on
  one: the guide states plainly that the lab's EEVEE timing
  inverts on real hardware, without having measured it.
- Production-resolution rendering, render farms, and Blender's
  add-on ecosystem; the neighbour tools of chapter 11
  (OpenSCAD beyond this series' own guide, FreeCAD, the
  commercial studios, game engines) — characterised, not run
  or benchmarked.

Fixtures are this guide's own and deliberately generic: a red
block, a blue ball, a green cone and a grey floor — no names,
organisations or real events. The rendered PNGs themselves are
not shipped in the repository; the transcripts carry their
measurements, which are the evidence the chapters rely on.
