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
# Ref #1: Across The Spider-Verse Wallpaper.svg
# ZERO CHARACTER ASSETS. ZERO POLYGON DECORATIONS.
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
      <rect x="650" y="40" width="910" height="620" rx="12" />
    </clipPath>
  </defs>

  <!-- LAYER 0: BACKGROUND ATMOSPHERE -->
  <rect width="1600" height="700" fill="url(#coverSky)" />
  <rect width="1600" height="700" fill="url(#coverHalftone)" />

  <!-- LAYER 1: INLINED REFERENCE ARTWORK #1 (PROMINENT 55% WIDTH, NATURAL ASPECT RATIO FIT) -->
  <rect x="646" y="36" width="918" height="628" fill="#120D1A" rx="14" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#heroArtClip)" opacity="0.95">
    <g transform="translate(650, 40) scale(0.95)">
      {ref1_inner}
    </g>
  </g>

  <!-- LAYER 2: LEFT SIDE TYPOGRAPHY & BRANDING (CLEAN RECTANGULAR FRAMES, NO POLYGONS) -->
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
print("Purified scene01-cover.svg generated (0 characters, 0 polygon shards).")

# ==============================================================================
# 2. SCENE 02: scene02-strip.svg
# Ref #2: Spider Man Into The Spider Verse Poster.svg
# ZERO CHARACTER ASSETS.
# ==============================================================================
ref2_inner = extract_inner_svg('assets/reference/Spider Man Into The Spider Verse Poster.svg', 'ref2')

scene02_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 480" width="100%" height="100%">
  <defs>
    <linearGradient id="stripSky" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E86A33" />
      <stop offset="50%" stop-color="#B83228" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="posterClip">
      <rect x="40" y="40" width="600" height="400" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="480" fill="url(#stripSky)" />

  <!-- LEFT SIDE ARTWORK PANEL (40% WIDTH WITH NATURAL FIT) -->
  <rect x="36" y="36" width="608" height="408" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#posterClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.75)">
      {ref2_inner}
    </g>
  </g>

  <!-- RIGHT NARRATIVE PANEL -->
  <g transform="translate(700, 80)">
    <rect x="0" y="0" width="840" height="320" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    
    <text x="40" y="60" font-family="'Impact', sans-serif" font-size="28" fill="#F5B041" letter-spacing="2">EVERY UNIVERSE STARTS WITH CURIOSITY.</text>

    <g font-family="'Courier New', monospace" font-size="15" fill="#F5F1E8">
      <text x="40" y="115">Mine started with a question:</text>
      <text x="40" y="150" font-weight="700" fill="#F5B041">"What if machines could retrieve knowledge, reason over context,</text>
      <text x="40" y="180" font-weight="700" fill="#E86A33">and safely act in real-world workflows?"</text>
      <text x="40" y="240" fill="#D0C4DF">A question became an experiment. Experiments became systems.</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene02-strip.svg', 'w', encoding='utf-8') as f:
    f.write(scene02_content)
print("Purified scene02-strip.svg generated (0 characters).")

# ==============================================================================
# 3. SCENE 03: scene03-rooftop.svg
# Ref #3: Spider-Man Homecoming PNG.svg
# ZERO CHARACTER ASSETS.
# ==============================================================================
ref3_inner = extract_inner_svg('assets/reference/Spider-Man_ Homecoming Film Series Marvel Cinematic Universe Spider-Man_ Homecoming Film Series Marvel Studios PNG.svg', 'ref3')

scene03_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 520" width="100%" height="100%">
  <defs>
    <linearGradient id="rooftopSunset" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#54152B" />
      <stop offset="60%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#1A0A1F" />
    </linearGradient>

    <clipPath id="homecomingClip">
      <rect x="40" y="40" width="680" height="440" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="520" fill="url(#rooftopSunset)" />

  <!-- LEFT SIDE ARTWORK PANEL (44% WIDTH) -->
  <rect x="36" y="36" width="688" height="448" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#homecomingClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.85)">
      {ref3_inner}
    </g>
  </g>

  <!-- RIGHT PHILOSOPHY PANEL -->
  <g transform="translate(780, 80)">
    <rect x="0" y="0" width="760" height="360" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    
    <text x="40" y="60" font-family="'Impact', sans-serif" font-size="32" fill="#F5B041" letter-spacing="2">THE ROOFTOP PERSPECTIVE</text>

    <g font-family="'Courier New', monospace" font-size="16" fill="#F5F1E8">
      <text x="40" y="125" font-weight="900" fill="#E86A33">"Every engineer sees a problem."</text>
      <text x="40" y="155" font-weight="900" fill="#F5B041">"I see a living system waiting to be understood."</text>

      <text x="40" y="225" fill="#F5F1E8">DESIGNATION: AI ENGINEER</text>
      <text x="40" y="255" fill="#F5F1E8">FOCUS: LLMs • RAG • AGENTIC SYSTEMS • LANGGRAPH</text>
      <text x="40" y="285" fill="#D0C4DF">LOCATION: EARTH-2705 // ONLINE</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene03-rooftop.svg', 'w', encoding='utf-8') as f:
    f.write(scene03_content)
print("Purified scene03-rooftop.svg generated (0 characters).")

# ==============================================================================
# 4. SCENE 05: scene05-leap.svg
# Ref #4: Spider Man_ Across The Spider Verse Wallpaper.svg
# ZERO CHARACTER ASSETS.
# ==============================================================================
ref4_inner = extract_inner_svg('assets/reference/Spider Man_ Across The Spider Verse Wallpaper.svg', 'ref4')

scene05_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 550" width="100%" height="100%">
  <defs>
    <linearGradient id="leapBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="50%" stop-color="#54152B" />
      <stop offset="100%" stop-color="#B83228" />
    </linearGradient>

    <clipPath id="leapRefClip">
      <rect x="40" y="40" width="820" height="470" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="550" fill="url(#leapBg)" />

  <!-- MIDGROUND REFERENCE ARTWORK PANEL (53% WIDTH) -->
  <rect x="36" y="36" width="828" height="478" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#leapRefClip)" opacity="0.95">
    <g transform="translate(40, -40) scale(0.85)">
      {ref4_inner}
    </g>
  </g>

  <!-- RIGHT PORTAL INTRODUCTION -->
  <g transform="translate(920, 90)">
    <rect x="0" y="0" width="620" height="370" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    
    <text x="40" y="60" font-family="'Impact', sans-serif" font-size="32" fill="#F5B041" letter-spacing="2">ENTER THE MULTIVERSE</text>
    <text x="40" y="95" font-family="'Courier New', monospace" font-size="15" fill="#E86A33" font-weight="900">// PROJECT UNIVERSES</text>

    <g font-family="'Courier New', monospace" font-size="15" fill="#F5F1E8">
      <text x="40" y="160">Every project is a distinct</text>
      <text x="40" y="190" font-weight="900" fill="#F5B041">multiverse dimension with its</text>
      <text x="40" y="220" font-weight="900" fill="#E86A33">own architectural story.</text>
      
      <text x="40" y="295" font-size="14" fill="#D0C4DF">LEAPING IN →</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene05-leap.svg', 'w', encoding='utf-8') as f:
    f.write(scene05_content)
print("Purified scene05-leap.svg generated (0 characters).")

# ==============================================================================
# 5. SCENE 08: scene08-ending.svg
# Ref #10: download (3).svg
# ZERO CHARACTER ASSETS.
# ==============================================================================
ref10_inner = extract_inner_svg('assets/reference/download (3).svg', 'ref10')

scene08_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 520" width="100%" height="100%">
  <defs>
    <linearGradient id="nightEnding" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="50%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#09040D" />
    </linearGradient>

    <clipPath id="endArtClip">
      <rect x="40" y="40" width="760" height="440" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="520" fill="url(#nightEnding)" />

  <!-- LEFT SIDE ARTWORK PANEL (48% WIDTH WITH NATURAL PROPORTION) -->
  <rect x="36" y="36" width="768" height="448" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g clip-path="url(#endArtClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.92)">
      {ref10_inner}
    </g>
  </g>

  <!-- RIGHT CINEMATIC ENDING TEXT PANEL -->
  <g transform="translate(840, 100)">
    <rect x="0" y="0" width="700" height="320" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    
    <text x="40" y="60" font-family="'Courier New', monospace" font-size="20" font-weight="900" fill="#F5B041">"Some systems answer questions."</text>
    <text x="40" y="105" font-family="'Impact', sans-serif" font-size="26" font-weight="900" fill="#F5F1E8" letter-spacing="2">"I WANT TO BUILD THE ONES THAT CHANGE WHAT HAPPENS NEXT."</text>

    <!-- TO BE CONTINUED BADGE -->
    <g transform="translate(40, 180)">
      <rect x="0" y="0" width="280" height="50" fill="#E86A33" rx="6" />
      <text x="140" y="33" font-family="'Impact', sans-serif" font-size="22" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">TO BE CONTINUED...</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene08-ending.svg', 'w', encoding='utf-8') as f:
    f.write(scene08_content)
print("Purified scene08-ending.svg generated (0 characters).")
