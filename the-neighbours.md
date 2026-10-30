# The Neighbours

**Outcome: you can place Blender among the other ways of
getting from an idea to a shape or a picture, and say what
each neighbour does that Blender doesn't — and the reverse.**

**Check: for each neighbour, name the job you'd hand it
instead of Blender.**

These tools are characterised from their documentation and
this series' other guides, not benchmarked here; nobody's
render times were harmed in this chapter.

## OpenSCAD — the shape as a program

OpenSCAD (a sibling guide in this series) builds solids the
way this guide builds scenes: as code, entirely. The
difference is what the code describes. OpenSCAD's language
*is* the model — cubes, spheres, unions and differences, with
variables for every dimension, and nothing else: no materials
worth the name, no lights, no camera artistry, and a preview
rather than a render. For a bracket whose dimensions must be
exact and adjustable, OpenSCAD is the sharper tool; for a
scene that must be *lit*, it has nothing to say. Blender is
the opposite trade — surfaces and appearances first, exactness
by discipline rather than by construction.

## The 3D printing pipeline — Blender as a supplier

The 3D Printing guide in this series turns model files into
plastic. Blender feeds that pipeline as a modelling source: it
exports the STL and OBJ files slicers eat, and its mesh tools
can repair and reshape models made elsewhere. The honest
caution travels with the handoff: Blender models are surfaces
that *look* solid, and a slicer wants solids that *are* — a
model can be beautiful in a render and unprintable in fact.
Different chapters of the two guides check different things;
the census method of chapter 7 has no opinion about whether a
mesh is watertight.

## Parametric CAD — FreeCAD and friends

FreeCAD (and its commercial cousins) model the way engineers
specify: sketches, constraints, dimensions that mean something,
and a history tree where changing a number rebuilds the part.
That is the right home for a part that must fit another part.
Blender can be made to model precisely, but precision is
something you bring to it, not something it keeps for you. In
exchange, CAD has no answer to "make it look like late
afternoon".

## The commercial studios — Maya, 3ds Max, Cinema 4D

The paid incumbents cover the same ground as Blender — often
deeper in the corners their industries pay for (character
rigs, film pipelines, support contracts, integration with a
studio's existing shelf of tools). The functional gap has
closed enough that Blender is credited on real productions;
the remaining differences are money, support, and incumbency
rather than a missing headline feature. A mere mortals guide
notes simply that the free tool is not the toy tool it once
was, and that skills transfer: scenes, materials, lights and
engines are the same ideas in every window.

## Game engines — Unreal, Unity

Game engines render scenes too, but their pictures are a means
to an interactive end: the scene must sustain sixty frames a
second while a player misbehaves in it. EEVEE borrows their
techniques for stills. If the deliverable moves and answers
back, start there; if it hangs on a wall (or a product page),
the renderer in this guide is the more direct tool.
