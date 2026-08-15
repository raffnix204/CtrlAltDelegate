# Flutter Performance & Rendering

Profile first. Distinguish UI-thread Dart work, raster/GPU work, rebuild frequency, layout/paint, image decode/cache and memory pressure.

`const`, builder-based lazy lists, bounded rebuild scope and explicit item extents can help when they reduce real work, but no single rule replaces profiling. `RepaintBoundary` trades memory/layers for repaint isolation and should be used on measured repaint hotspots.

Test on representative slower devices when frame budget matters.
