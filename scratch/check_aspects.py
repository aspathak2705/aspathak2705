import os
import re

ref_folder = 'assets/reference'
print("=== NATIVE ASPECT RATIOS OF REFERENCE SVG ASSETS ===")
for f in os.listdir(ref_folder):
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
        
        aspect = "Unknown"
        if vb:
            parts = [float(x) for x in vb.replace(',', ' ').split() if x.strip()]
            if len(parts) == 4 and parts[3] != 0:
                ratio = parts[2] / parts[3]
                aspect = f"{ratio:.2f} ({int(parts[2])}x{int(parts[3])})"
        elif w and h:
            try:
                w_val = float(re.sub(r'[^\d.]', '', w))
                h_val = float(re.sub(r'[^\d.]', '', h))
                ratio = w_val / h_val
                aspect = f"{ratio:.2f} ({int(w_val)}x{int(h_val)})"
            except Exception as e:
                pass
        
        print(f"{f:<65} | Aspect: {aspect}")
