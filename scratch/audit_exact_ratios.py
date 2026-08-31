import os
import re

scenes = [
    ('scene01-cover.svg', 600, 1200),
    ('scene02-strip.svg', 683, 1024),
    ('scene03-rooftop.svg', 728, 1234),
    ('scene05-leap.svg', 736, 331),
    ('project-meravyapar.svg', 736, 736),
    ('project-forgemind.svg', 736, 1308),
    ('project-autohr.svg', 735, 324),
    ('mission-control.svg', 736, 414),
    ('multiverse-city.svg', 734, 307),
    ('scene08-ending.svg', 736, 434)
]

print("=== EXACT MATHEMATICAL ASPECT RATIO AUDIT (COMPARING NATIVE VS FRAME) ===")
for s, native_w, native_h in scenes:
    path = os.path.join('assets/scenes', s)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract rect in clipPath
    clip_rect = re.search(r'<clipPath id="[^"]+">\s*<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', content)
    if clip_rect:
        fw = float(clip_rect.group(3))
        fh = float(clip_rect.group(4))
        
        native_ratio = native_w / native_h
        frame_ratio = fw / fh
        diff = abs(native_ratio - frame_ratio)
        
        print(f"{s:<24} | Native: {native_ratio:.4f} | Frame ({fw:.1f}x{fh:.1f}): {frame_ratio:.4f} | Diff: {diff:.4f} | MATCH: {diff < 0.001}")
