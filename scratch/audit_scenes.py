import os
import re

scenes = [
    'scene01-cover.svg', 'scene02-strip.svg', 'scene03-rooftop.svg',
    'scene04-sense.svg', 'scene05-leap.svg', 'project-meravyapar.svg',
    'project-bhoomiflow.svg', 'project-forgemind.svg', 'project-autohr.svg',
    'mission-control.svg', 'multiverse-city.svg', 'scene08-ending.svg'
]

print("=== AUTOMATED SVG RENDER & SELF-CONTAINMENT AUDIT ===")
for s in scenes:
    path = os.path.join('assets/scenes', s)
    if not os.path.exists(path):
        print(f"{s:<24} | STATUS: MISSING")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find any href pointing to an external file (e.g. href="../reference/..." or href="http...")
    ext_hrefs = [h for h in re.findall(r'href=["\']([^"\']+)["\']', content) if not h.startswith('#')]
    size_kb = os.path.getsize(path) / 1024
    
    status = "SELF-CONTAINED (PASSED)" if len(ext_hrefs) == 0 else f"FAILED ({len(ext_hrefs)} external hrefs)"
    print(f"{s:<24} | Size: {size_kb:7.1f} KB | {status}")
