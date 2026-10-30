# Installing Blender

**Outcome: Blender is on the machine, the download is proven
untampered, and the program answers a version check.**

**Check:**

```
$ blender --version
Blender 4.5.9 LTS
```

Blender is distributed from blender.org. On Linux the official
form is a single compressed archive — no installer, no package
manager required: download it, unpack it, and the `blender`
program inside runs. (Windows and macOS have ordinary
installers from the same download page; everything after this
chapter is identical on all three.)

## The lab's install, exactly

The lab used the 4.5 LTS line — LTS means *long-term support*:
a release the project keeps fixing for two years, which is the
sane choice for following a guide. The archive:

```
$ sha256sum blender-4.5.9-linux-x64.tar.xz; ls -la blender-4.5.9-linux-x64.tar.xz
dcdc3eca6c9825bb35a8033b689c053f3cb5a9b0cd2a61b2eac2a49436b4ad3d  blender-4.5.9-linux-x64.tar.xz
-rw-rw---- 1 root root 377929956 Oct 30 08:23 blender-4.5.9-linux-x64.tar.xz
```

Two habits are packed into those two lines:

- **Size first.** The archive is about 378 MB. A download that
  arrives at a few kilobytes is not Blender — it is an error
  page wearing Blender's name, and unpacking it will fail in
  confusing ways. Check the size before anything else.
- **Checksum against the publisher's.** The download page
  publishes a SHA-256 for each file. The hash printed above is
  what the lab's machine computed for the file it actually
  ran; on your machine, compare yours against the value on the
  release page, not against this book — a hash copied from a
  guide proves the guide's download, not yours.

Unpack it wherever you keep programs:

```
tar -xf blender-4.5.9-linux-x64.tar.xz
```

That produces a folder `blender-4.5.9-linux-x64/` with the
`blender` executable inside, alongside helpers (including
`blender-softwaregl`, a launcher that forces software graphics
— chapter 8 meets the situation it exists for). No step in the
install needs administrator rights, and nothing is written
outside the folder. To "uninstall" later, delete the folder.

## Prove it runs

```
$ blender --version
Blender 4.5.9 LTS
	build date: 2026-04-21
	build commit date: 2026-04-20
	build hash: 8bf95cbd38d1
	build branch: blender-v4.5-release
	build platform: Linux
	build type: Release
	... (compiler flags omitted)
```

The check matters because `--version` exercises the real
program, not a launcher script's opinion of it. The build hash
is the precise source revision; you will likely never need it,
but bug reports will ask, and here is where it lives.

One environment note that shapes the whole guide: the lab
machine has **no display and no graphics card**. That rules
nothing in this chapter out — the archive runs fine headless —
but it decides how the rest of the guide works: everything is
done in background mode (`blender -b ...`), and one of the
three engines will have to improvise. Chapter 8 shows what it
did.

*Transcript: `blender-lab/transcripts/t00-version-and-default-scene.txt`.*
