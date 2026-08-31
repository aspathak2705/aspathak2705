import os
import re

ref_folder = 'assets/reference'
print("=== NATIVE PIXEL DIMENSIONS & EXACT ASPECT RATIOS ===")
for f in sorted(os.listdir(ref_folder)):
    if f.endswith('.svg'):
        path = os.path.join(ref_folder, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        viewbox_match = re.search(r'viewBox=["\']([^"\']+)["\']', content)
        width_match = re.search(r'width=["\']([^"\']+)["\']', content)
        height_match = re.search(r'height=["\']([^"\']+)["\']', content)
        
        vb = viewbox_match.group(1) if viewbox_match else None
        w = width_match.group(1) if width_match else None
        h = height_match.group(1) if height_match else None
        
        if vb:
            parts = [float(x) for x in vb.replace(',', ' ').split() if x.strip()]
            print(f"{f:<65} | viewBox: {parts[2]} x {parts[3]} -> Ratio: {parts[2]/parts[3]:.4f}")
        elif w and h:
            w_val = float(re.sub(r'[^\d.]', '', w))
            h_val = float(re.sub(r'[^\d.]', '', h))
            print(f"{f:<65} | WxH: {w_val} x {h_val} -> Ratio: {w_val/h_val:.4f}")
