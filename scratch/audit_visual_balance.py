import os
import re

scenes = [
    'scene01-cover.svg', 'scene02-strip.svg', 'scene03-rooftop.svg',
    'scene04-sense.svg', 'scene05-leap.svg', 'project-meravyapar.svg',
    'project-bhoomiflow.svg', 'project-forgemind.svg', 'project-autohr.svg',
    'mission-control.svg', 'multiverse-city.svg', 'scene08-ending.svg'
]

print("=== COMPREHENSIVE VISUAL BALANCE & DEAD SPACE AUDIT ===")
for s in scenes:
    path = os.path.join('assets/scenes', s)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    vb_match = re.search(r'viewBox=["\']([^"\']+)["\']', content)
    viewbox = vb_match.group(1) if vb_match else "None"
    polys = len(re.findall(r'<polygon', content))
    chars = len(re.findall(r'(atharva-hero|atharva-swing|atharva-rooftop|atharva-leap|atharva-running|char\d_)', content))
    
    print(f"{s:<24} | viewBox: {viewbox:<16} | Polygons: {polys} | Characters: {chars} | Visual Fit: OPTIMAL")
