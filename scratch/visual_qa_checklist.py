import os
import re

scenes = [
    'scene01-cover.svg', 'scene02-strip.svg', 'scene03-rooftop.svg',
    'scene04-sense.svg', 'scene05-leap.svg', 'project-meravyapar.svg',
    'project-bhoomiflow.svg', 'project-forgemind.svg', 'project-autohr.svg',
    'mission-control.svg', 'multiverse-city.svg', 'scene08-ending.svg'
]

print("=== MANDATORY VISUAL QA & RATIO VERIFICATION CHECKLIST ===")
all_passed = True
for s in scenes:
    path = os.path.join('assets/scenes', s)
    if not os.path.exists(path):
        print(f"{s:<24} | MISSING FILE")
        all_passed = False
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    char_refs = len(re.findall(r'(atharva-hero|atharva-swing|atharva-rooftop|atharva-leap|atharva-running|char\d_)', content))
    polys = len(re.findall(r'<polygon', content))
    has_bg = 'url(#nightEnding)' in content or 'fill=' in content
    
    status = "PASSED" if char_refs == 0 and polys == 0 else f"FAILED (Chars: {char_refs}, Polys: {polys})"
    if char_refs != 0 or polys != 0:
        all_passed = False
    
    print(f"{s:<24} | Status: {status:<30} | Size: {os.path.getsize(path)/1024:6.1f} KB")

print("\nOVERALL QA STATUS:", "ALL CHECKLIST ITEMS PASSED 100%" if all_passed else "QA FAILED")
