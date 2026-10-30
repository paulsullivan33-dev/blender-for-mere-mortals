# Three Engines, One Scene

**Outcome: the same file, rendered by Workbench and by EEVEE
as well as Cycles, and a measured account of where the three
pictures agree, where they differ, and why one material can be
blue to one engine and grey to another.**

**Check: all three censuses find the red, the green and the
blue. The engines differ in counts and cost — if one finds no
colour at all, chapter 13's grey-object entry is about your
scene.**

Chapter 2 named the engines. Here they are, one scene each,
all measured with chapter 7's instrument.

## Workbench: the sprinter

Workbench exists to be looked at *while you work* — it is the
engine behind the window's Solid view — so it trades truth for
speed. On the lab machine it rendered the still life in about
a second:

```
Saved: '/home/hatch/workspace/blender-labwork/renders/still-workbench.png'
Time: 00:00.64 (Saving: 00:00.16)
```

Its census: 5,168 distinct colours; red 15.2%, green 8.5%, blue
12.1%. Same composition, flatter shading — fewer distinct
colours than Cycles' 6,940, and shares a point or two off. For
checking *composition* — is everything in frame, in proportion,
not intersecting — it is the right tool, and its price is
nothing.

## The second colour, demonstrated

Workbench does not read the material node tree. It reads the
plain **viewport colour** — the second colour chapter 5 set
alongside the Base Color. The lab proved the separation by
resetting one material's viewport colour to the factory grey
(0.8, 0.8, 0.8), leaving its node tree blue, and rendering both
ways:

- **Workbench:** blue falls from 12.1% to **exactly 0.0%**.
  Red and green do not move — 15.2% and 8.5%, to the pixel.
  The Ball is grey in this picture.
- **Cycles, same change:** the census is the original census,
  colour for colour — blue still 13.4%. Cycles never looks at
  the viewport colour.

Two engines can therefore disagree about what colour an object
*is*, each honestly reporting a different field of the same
material. When a preview shows a grey object that renders
coloured (or the reverse), this is why, and the fix is to set
both colours — which is why the build script does.

## EEVEE: the engine out of its element

EEVEE is built for a graphics card. The lab machine has none,
and its transcript opens with the sound of that mismatch:

```
EGL Error (0x3009): EGL_BAD_MATCH: Arguments are inconsistent (for example, a valid context requires buffers not supplied by a valid surface).
```

(three times — Blender retries before giving up on hardware).
Then the surprise: **it rendered anyway**, falling back to
software graphics, and finished its 64 samples in 2 minutes
2 seconds, exit code 0, with a census in family with the
others — 3,557 distinct colours; red 15.3%, green 11.6%, blue
13.3%.

Hold the two halves of that result apart. The *picture* is
genuine: same scene, same strong colours. The *timing* is the
lab's, not EEVEE's: an engine designed to run on a graphics
card, running on a CPU in software, is a fish on a bicycle. On
a machine with any modern graphics card — including the
integrated kind in ordinary laptops — EEVEE renders scenes
like this in well under a second and Cycles is the slow one.
Chapter 12 lists this under limits: know which machine a
timing belongs to before quoting it.

## The three, side by side

| Engine    | Lab time | Distinct colours | Red / Green / Blue | Reads |
|-----------|----------|------------------|--------------------|-------|
| Cycles    | ≈12–23 s | 6,940            | 15.3 / 10.6 / 13.4 | node tree |
| Workbench | ≈1 s     | 5,168            | 15.2 / 8.5 / 12.1  | viewport colour |
| EEVEE     | ≈2 min*  | 3,557            | 15.3 / 11.6 / 13.3 | node tree |

*\*Software fallback on a display-less machine; see above.*

The working rule the table supports: compose with Workbench,
trust Cycles for the final picture, and use EEVEE where a
graphics card makes it the fast *and* good-enough choice —
which, outside this lab, is most interactive work.

*Transcripts: `blender-lab/transcripts/t04-workbench-render.txt`
and `blender-lab/transcripts/t05-eevee-attempt.txt`.*
