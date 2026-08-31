import os
import re

def extract_inner_svg(file_path, prefix=""):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Prefix IDs to avoid DOM collisions
    if prefix:
        def replace_id(match):
            id_name = match.group(1)
            return f'id="{prefix}_{id_name}"'
        content = re.sub(r'id="([^"]+)"', replace_id, content)
        def replace_url(match):
            url_name = match.group(1)
            return f'url(#{prefix}_{url_name})'
        content = re.sub(r'url\(#([^)]+)\)', replace_url, content)
        def replace_href(match):
            href_name = match.group(1)
            return f'href="#{prefix}_{href_name}"'
        content = re.sub(r'href="#([^"]+)"', replace_href, content)

    content = re.sub(r'<\?xml.*?\?>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!DOCTYPE.*?>', '', content, flags=re.DOTALL)
    
    svg_match = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
    if svg_match:
        return svg_match.group(1).strip()
    return content.strip()

# ==============================================================================
# 1. SCENE 01: scene01-cover.svg
# Ref #1: Across The Spider-Verse Wallpaper.svg (Native: 600x1200, Ratio: 0.5000)
# Frame: 310px wide x 620px tall -> Ratio: 310/620 = 0.5000 EXACT
# ==============================================================================
ref1_inner = extract_inner_svg('assets/reference/Across The Spider-Verse Wallpaper.svg', 'ref1')

scene01_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 700" width="100%" height="100%">
  <defs>
    <linearGradient id="coverSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="40%" stop-color="#54152B" />
      <stop offset="80%" stop-color="#B83228" />
      <stop offset="100%" stop-color="#E86A33" />
    </linearGradient>

    <pattern id="coverHalftone" x="0" y="0" width="12" height="12" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.5" fill="#F5B041" fill-opacity="0.2" />
    </pattern>

    <clipPath id="heroArtClip">
      <rect x="1210" y="40" width="310" height="620" rx="12" />
    </clipPath>
  </defs>

  <!-- LAYER 0: BACKGROUND ATMOSPHERE -->
  <rect width="1600" height="700" fill="url(#coverSky)" />
  <rect width="1600" height="700" fill="url(#coverHalftone)" />

  <!-- LAYER 1: INLINED PORTRAIT REFERENCE ARTWORK #1 (FRAME EXACTLY MATCHED TO 0.5000 RATIO: 310x620) -->
  <rect x="1206" y="36" width="318" height="628" fill="#120D1A" rx="14" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#heroArtClip)" opacity="0.95">
    <g transform="translate(1210, 40) scale(0.516667)">
      {ref1_inner}
    </g>
  </g>

  <!-- LAYER 2: LEFT SIDE TYPOGRAPHY & BRANDING (BALANCED PROPORTIONS) -->
  <g transform="translate(80, 70)">
    <rect x="0" y="0" width="380" height="42" fill="#E86A33" rx="4" />
    <text x="190" y="27" font-family="'Courier New', monospace" font-size="15" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">ISSUE #01 // ATHARVA'S UNIVERSE</text>
  </g>

  <g transform="translate(80, 240)">
    <text x="4" y="4" font-family="'Impact', 'Arial Black', sans-serif" font-size="120" font-weight="900" letter-spacing="8" fill="#1A0A1F">ATHARVA</text>
    <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="120" font-weight="900" letter-spacing="8" fill="#F5F1E8">ATHARVA</text>

    <text x="4" y="124" font-family="'Impact', 'Arial Black', sans-serif" font-size="120" font-weight="900" letter-spacing="8" fill="#1A0A1F">PATHAK</text>
    <text x="0" y="120" font-family="'Impact', 'Arial Black', sans-serif" font-size="120" font-weight="900" letter-spacing="8" fill="#F5B041">PATHAK</text>
  </g>

  <g transform="translate(80, 480)">
    <rect x="0" y="0" width="440" height="50" fill="#F5B041" rx="4" />
    <text x="220" y="34" font-family="'Impact', sans-serif" font-size="28" font-weight="900" letter-spacing="4" text-anchor="middle" fill="#1A0A1F">★ AI ENGINEER ★</text>
  </g>

  <g transform="translate(80, 565)">
    <rect x="0" y="0" width="540" height="70" fill="#1A0A1F" stroke="#F5F1E8" stroke-width="2" rx="6" />
    <text x="25" y="30" font-family="'Courier New', monospace" font-size="15" font-weight="900" fill="#F5B041">"BUILDING SYSTEMS THAT REMEMBER, REASON &amp; ACT."</text>
    <text x="25" y="52" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8" font-style="italic">With great curiosity comes great responsibility.</text>
  </g>
</svg>'''

with open('assets/scenes/scene01-cover.svg', 'w', encoding='utf-8') as f:
    f.write(scene01_content)
print("Exact 0.5000 ratio scene01-cover.svg generated.")

# ==============================================================================
# 2. MULTIVERSE CITY: multiverse-city.svg
# Ref #6: MUMBATTAN.svg (Native: 734x307, Ratio: 2.3909)
# Frame: 1520px wide x 635.7px tall -> Ratio: 1520 / 635.7 = 2.3909 EXACT
# Canvas height extended to 950px to accommodate full-size 2.3909 banner + 4 district cards below
# ==============================================================================
ref6_inner = extract_inner_svg('assets/reference/MUMBATTAN.svg', 'ref6')

city_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 950" width="100%" height="100%">
  <defs>
    <linearGradient id="cityDistrictBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="35%" stop-color="#54152B" />
      <stop offset="65%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#E86A33" />
    </linearGradient>

    <clipPath id="mumbattanClip">
      <rect x="40" y="40" width="1520" height="635.7" rx="12" />
    </clipPath>
  </defs>

  <rect width="1600" height="950" fill="url(#cityDistrictBg)" />
  
  <!-- PANORAMIC ARTWORK HEADER MATCHING 2.3909 RATIO EXACTLY (1520x635.7) -->
  <rect x="36" y="36" width="1528" height="643.7" fill="#120D1A" rx="14" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#mumbattanClip)" opacity="0.95">
    <g transform="translate(40, 40) scale(2.070845)">
      {ref6_inner}
    </g>
  </g>

  <!-- FOUR DISTRICT CARDS BELOW PANORAMIC HEADER -->
  <g transform="translate(40, 700)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="360" height="210" fill="#1A0A1F" opacity="0.95" stroke="#E86A33" stroke-width="2" rx="10" />
      <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#E86A33" letter-spacing="1">FINANCIAL DISTRICT</text>
      <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#F5B041">// MeraVyapar AI</text>
      <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Fragmented transaction signals</text>
      <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">&amp; evidence graph engine.</text>
    </g>

    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="360" height="210" fill="#1A0A1F" opacity="0.95" stroke="#F5B041" stroke-width="2" rx="10" />
      <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#F5B041" letter-spacing="1">DOCUMENT DISTRICT</text>
      <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#E86A33">// BhoomiFlow</text>
      <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Land case evidence integrity</text>
      <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">&amp; legal document RAG.</text>
    </g>

    <g transform="translate(770, 0)">
      <rect x="0" y="0" width="360" height="210" fill="#1A0A1F" opacity="0.95" stroke="#54152B" stroke-width="2" rx="10" />
      <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#F5F1E8" letter-spacing="1">CODEBASE DISTRICT</text>
      <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#F5B041">// ForgeMind</text>
      <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Repository intelligence &amp; issue</text>
      <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">triaging copilot.</text>
    </g>

    <g transform="translate(1155, 0)">
      <rect x="0" y="0" width="365" height="210" fill="#1A0A1F" opacity="0.95" stroke="#E86A33" stroke-width="2" rx="10" />
      <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#E86A33" letter-spacing="1">AUTOMATION DISTRICT</text>
      <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#F5B041">// AutoHR</text>
      <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Automated meeting workflows</text>
      <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">&amp; induction narration.</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/multiverse-city.svg', 'w', encoding='utf-8') as f:
    f.write(city_content)
print("Exact 2.3909 ratio multiverse-city.svg generated.")
