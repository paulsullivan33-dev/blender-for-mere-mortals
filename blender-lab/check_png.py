"""Measure a rendered PNG instead of trusting it: dimensions,
how many distinct colours it holds, its five commonest colours,
and its average colour. With two files, also count the pixels
that differ and report where they are and how the changed area's
average colour moved.

    python3 check_png.py still.png
    python3 check_png.py before.png after.png
"""

import sys
from collections import Counter

from PIL import Image


def describe(path):
    img = Image.open(path).convert("RGB")
    colours = Counter(img.getdata())
    total = img.width * img.height
    print("%s" % path)
    print("  size: %d x %d (%d pixels)" % (img.width, img.height, total))
    print("  distinct colours: %d" % len(colours))
    print("  five commonest colours (RGB, count, share):")
    for rgb, count in colours.most_common(5):
        print("    %s  %6d  %5.1f%%" % (rgb, count, 100.0 * count / total))
    strong = {"red": 0, "green": 0, "blue": 0}
    for (r, g, b) in img.getdata():
        if r - max(g, b) >= 40:
            strong["red"] += 1
        elif g - max(r, b) >= 40:
            strong["green"] += 1
        elif b - max(r, g) >= 40:
            strong["blue"] += 1
    print("  strongly coloured pixels (one channel ahead by 40+):")
    for name in ("red", "green", "blue"):
        print("    %-6s %6d  %5.1f%%" % (name, strong[name], 100.0 * strong[name] / total))
    return img


def region_mean(img, box):
    region = img.crop(box)
    pixels = list(region.getdata())
    n = len(pixels)
    return tuple(round(sum(p[c] for p in pixels) / n, 1) for c in range(3))


def compare(a, b):
    assert a.size == b.size, "pictures differ in size"
    pa, pb = a.load(), b.load()
    w, h = a.size
    exact = 0
    changed = []
    for y in range(h):
        for x in range(w):
            if pa[x, y] != pb[x, y]:
                exact += 1
                delta = max(abs(pa[x, y][c] - pb[x, y][c]) for c in range(3))
                if delta > 10:
                    changed.append((x, y))
    total = w * h
    print("comparison:")
    print("  pixels differing at all: %d of %d (%.1f%%)" % (exact, total, 100.0 * exact / total))
    print("  pixels differing by more than 10 in some channel: %d (%.1f%%)"
          % (len(changed), 100.0 * len(changed) / total))
    if changed:
        xs = [p[0] for p in changed]
        ys = [p[1] for p in changed]
        box = (min(xs), min(ys), max(xs) + 1, max(ys) + 1)
        print("  bounding box of the material change: x %d..%d, y %d..%d" % (box[0], box[2] - 1, box[1], box[3] - 1))
        print("  average colour inside the box, before: %s" % (region_mean(a, box),))
        print("  average colour inside the box, after:  %s" % (region_mean(b, box),))


first = describe(sys.argv[1])
if len(sys.argv) > 2:
    second = describe(sys.argv[2])
    compare(first, second)
