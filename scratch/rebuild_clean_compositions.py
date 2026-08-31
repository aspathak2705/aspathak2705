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

    # Strip <?xml ... ?>, <!DOCTYPE ... >, and outer <svg> tag
    content = re.sub(r'<\?xml.*?\?>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!DOCTYPE.*?>', '', content, flags=re.DOTALL)
    
    svg_match = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
    if svg_match:
        return svg_match.group(1).strip()
    return content.strip()

# ==============================================================================
# 1. SCENE 01: scene01-cover.svg
# Ref #1: Across The Spider-Verse Wallpaper.svg
# Char #1: atharva-hero.svg
# ==============================================================================
ref1_inner = extract_inner_svg('assets/reference/Across The Spider-Verse Wallpaper.svg', 'ref1')
char1_inner = extract_inner_svg('assets/characters/atharva-hero.svg', 'char1')

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
      <rect x="700" y="40" width="860" height="620" rx="12" />
    </clipPath>
  </defs>

  <!-- LAYER 0: BACKGROUND GRADIENT & SUNSET ATMOSPHERE -->
  <rect width="1600" height="700" fill="url(#coverSky)" />
  <rect width="1600" height="700" fill="url(#coverHalftone)" />

  <!-- LAYER 1: INLINED REFERENCE ARTWORK #1 (RIGHT SIDE 55% CANVASES WITH NATURAL ASPECT RATIO) -->
  <g clip-path="url(#heroArtClip)" opacity="0.95">
    <g transform="translate(680, 20) scale(0.95)">
      {ref1_inner}
    </g>
  </g>

  <!-- LAYER 2: INLINED ATHARVA HERO CHARACTER #1 (FOREGROUND OVERLAP) -->
  <g transform="translate(640, 180) scale(0.7)">
    {char1_inner}
  </g>

  <!-- LAYER 3: LEFT SIDE TYPOGRAPHY PANEL (NO RANDOM POLYGONS) -->
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
    <rect x="0" y="0" width="560" height="70" fill="#1A0A1F" stroke="#F5F1E8" stroke-width="2" rx="6" />
    <text x="25" y="30" font-family="'Courier New', monospace" font-size="15" font-weight="900" fill="#F5B041">"BUILDING SYSTEMS THAT REMEMBER, REASON &amp; ACT."</text>
    <text x="25" y="52" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8" font-style="italic">With great curiosity comes great responsibility.</text>
  </g>
</svg>'''

with open('assets/scenes/scene01-cover.svg', 'w', encoding='utf-8') as f:
    f.write(scene01_content)
print("Clean scene01-cover.svg generated.")

# ==============================================================================
# 2. SCENE 02: scene02-strip.svg
# Ref #2: Spider Man Into The Spider Verse Poster.svg
# Char #2: atharva-swing.svg
# ==============================================================================
ref2_inner = extract_inner_svg('assets/reference/Spider Man Into The Spider Verse Poster.svg', 'ref2')
char2_inner = extract_inner_svg('assets/characters/atharva-swing.svg', 'char2')

scene02_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 480" width="100%" height="100%">
  <defs>
    <linearGradient id="stripSky" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E86A33" />
      <stop offset="50%" stop-color="#B83228" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="posterClip">
      <rect x="40" y="40" width="540" height="400" rx="10" />
    </clipPath>

    <style>
      @keyframes swingMove {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(25px, -15px); }}
        100% {{ transform: translate(0, 0); }}
      }}
      .anim-swing {{ animation: swingMove 4s ease-in-out infinite; }}
    </style>
  </defs>

  <rect width="1600" height="480" fill="url(#stripSky)" />

  <!-- LEFT SIDE ARTWORK PANEL (38% WIDTH WITH NATURAL FIT) -->
  <rect x="36" y="36" width="548" height="408" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#posterClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.72)">
      {ref2_inner}
    </g>
  </g>

  <!-- FOREGROUND SWING CHARACTER OVERLAPPING BOUNDARY -->
  <g transform="translate(540, 60)" class="anim-swing">
    <g transform="scale(0.55)">
      {char2_inner}
    </g>
  </g>

  <path d="M 720,190 Q 1050,300 1550,140" stroke="#F5B041" stroke-width="4" stroke-dasharray="10,5" fill="none" />

  <!-- RIGHT NARRATIVE PANEL -->
  <g transform="translate(860, 80)">
    <rect x="0" y="0" width="680" height="320" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    
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
print("Clean scene02-strip.svg generated.")

# ==============================================================================
# 3. SCENE 03: scene03-rooftop.svg
# Ref #3: Spider-Man Homecoming PNG.svg
# Char #3: atharva-rooftop.svg
# ==============================================================================
ref3_inner = extract_inner_svg('assets/reference/Spider-Man_ Homecoming Film Series Marvel Cinematic Universe Spider-Man_ Homecoming Film Series Marvel Studios PNG.svg', 'ref3')
char3_inner = extract_inner_svg('assets/characters/atharva-rooftop.svg', 'char3')

scene03_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 520" width="100%" height="100%">
  <defs>
    <linearGradient id="rooftopSunset" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#54152B" />
      <stop offset="60%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#1A0A1F" />
    </linearGradient>

    <clipPath id="homecomingClip">
      <rect x="40" y="40" width="650" height="440" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="520" fill="url(#rooftopSunset)" />

  <!-- LEFT SIDE ARTWORK PANEL (42% WIDTH) -->
  <rect x="36" y="36" width="658" height="448" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#homecomingClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.82)">
      {ref3_inner}
    </g>
  </g>

  <!-- FOREGROUND ROOFTOP CHARACTER -->
  <g transform="translate(540, 90)">
    <g transform="scale(0.58)">
      {char3_inner}
    </g>
  </g>

  <!-- RIGHT PHILOSOPHY PANEL -->
  <g transform="translate(860, 80)">
    <rect x="0" y="0" width="680" height="360" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    
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
print("Clean scene03-rooftop.svg generated.")

# ==============================================================================
# 4. SCENE 05: scene05-leap.svg
# Ref #4: Spider Man_ Across The Spider Verse Wallpaper.svg
# Char #4: atharva-leap.svg
# ==============================================================================
ref4_inner = extract_inner_svg('assets/reference/Spider Man_ Across The Spider Verse Wallpaper.svg', 'ref4')
char4_inner = extract_inner_svg('assets/characters/atharva-leap.svg', 'char4')

scene05_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 550" width="100%" height="100%">
  <defs>
    <linearGradient id="leapBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="50%" stop-color="#54152B" />
      <stop offset="100%" stop-color="#B83228" />
    </linearGradient>

    <clipPath id="leapRefClip">
      <rect x="40" y="40" width="680" height="470" rx="10" />
    </clipPath>

    <style>
      @keyframes leapMotion {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(25px, -20px); }}
        100% {{ transform: translate(0, 0); }}
      }}
      .anim-leap {{ animation: leapMotion 3.5s ease-in-out infinite; }}
    </style>
  </defs>

  <rect width="1600" height="550" fill="url(#leapBg)" />

  <!-- MIDGROUND REFERENCE ARTWORK PANEL -->
  <rect x="36" y="36" width="688" height="478" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#leapRefClip)" opacity="0.95">
    <g transform="translate(40, -40) scale(0.82)">
      {ref4_inner}
    </g>
  </g>

  <!-- FOREGROUND ATHARVA LEAP CHARACTER -->
  <g transform="translate(660, 60)" class="anim-leap">
    <g transform="scale(0.62)">
      {char4_inner}
    </g>
  </g>

  <path d="M 960,260 Q 1250,380 1550,220" stroke="#F5B041" stroke-width="5" stroke-dasharray="10,5" fill="none" />

  <!-- RIGHT PORTAL INTRODUCTION -->
  <g transform="translate(1060, 90)">
    <rect x="0" y="0" width="480" height="370" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    
    <text x="35" y="60" font-family="'Impact', sans-serif" font-size="30" fill="#F5B041" letter-spacing="2">ENTER THE MULTIVERSE</text>
    <text x="35" y="95" font-family="'Courier New', monospace" font-size="15" fill="#E86A33" font-weight="900">// PROJECT UNIVERSES</text>

    <g font-family="'Courier New', monospace" font-size="15" fill="#F5F1E8">
      <text x="35" y="160">Every project is a distinct</text>
      <text x="35" y="190" font-weight="900" fill="#F5B041">multiverse dimension with its</text>
      <text x="35" y="220" font-weight="900" fill="#E86A33">own architectural story.</text>
      
      <text x="35" y="295" font-size="14" fill="#D0C4DF">LEAPING IN →</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene05-leap.svg', 'w', encoding='utf-8') as f:
    f.write(scene05_content)
print("Clean scene05-leap.svg generated.")

# ==============================================================================
# 5. PROJECT 01: project-meravyapar.svg (Ref #5: download (4).svg)
# ==============================================================================
ref5_inner = extract_inner_svg('assets/reference/download (4).svg', 'ref5')

project_mv_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="mvArtClip">
      <rect x="40" y="40" width="520" height="420" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#p1Grad)" />

  <!-- STANDARDIZED PROJECT ARTWORK PANEL (LEFT ~36% WIDTH) -->
  <rect x="36" y="36" width="528" height="428" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g clip-path="url(#mvArtClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.72)">
      {ref5_inner}
    </g>
  </g>

  <!-- CONTENT PANEL (RIGHT ~64% WIDTH) -->
  <g transform="translate(600, 45)">
    <rect x="0" y="0" width="940" height="410" fill="#1A0A1F" stroke="#E86A33" stroke-width="2" rx="12" />

    <rect x="35" y="25" width="540" height="50" fill="#E86A33" rx="4" />
    <text x="55" y="60" font-family="'Impact', sans-serif" font-size="32" font-weight="900" fill="#F5F1E8" letter-spacing="3">UNIVERSE 01 // MERAVYAPAR AI</text>

    <g transform="translate(35, 95)">
      <text x="0" y="25" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#F5B041">"Money leaves clues. Intelligent systems learn to follow them."</text>
      
      <g font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8" transform="translate(0, 50)">
        <text x="0" y="0">AI Financial Autopilot for merchants parsing fragmented transactions,</text>
        <text x="0" y="25">evidence-driven reconciliation, receivables prioritization, and payment promises.</text>
      </g>

      <g transform="translate(0, 120)" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
        <circle cx="10" cy="0" r="4" fill="#E86A33" />
        <text x="25" y="4">Financial Intelligence Graph &amp; Transaction Evidence</text>

        <circle cx="10" cy="30" r="4" fill="#F5B041" />
        <text x="25" y="34">Receivables Prioritization &amp; Payment Promise Tracking</text>

        <circle cx="10" cy="60" r="4" fill="#F5F1E8" />
        <text x="25" y="64">Agentic Financial Analysis Pipeline</text>
      </g>

      <g transform="translate(0, 220)" font-family="'Courier New', monospace" font-size="12" fill="#F5F1E8">
        <rect x="0" y="0" width="110" height="30" fill="#2D112C" stroke="#E86A33" stroke-width="1.5" rx="3" />
        <text x="55" y="20" text-anchor="middle">FASTAPI</text>

        <rect x="125" y="0" width="130" height="30" fill="#2D112C" stroke="#F5B041" stroke-width="1.5" rx="3" />
        <text x="190" y="20" text-anchor="middle">LANGGRAPH</text>

        <rect x="270" y="0" width="130" height="30" fill="#2D112C" stroke="#F5F1E8" stroke-width="1.5" rx="3" />
        <text x="335" y="20" text-anchor="middle">POSTGRESQL</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/scenes/project-meravyapar.svg', 'w', encoding='utf-8') as f:
    f.write(project_mv_content)
print("Clean project-meravyapar.svg generated.")

# ==============================================================================
# 6. PROJECT 03: project-forgemind.svg (Ref #7: download (5).svg)
# ==============================================================================
ref7_inner = extract_inner_svg('assets/reference/download (5).svg', 'ref7')

project_fm_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="fmArtClip">
      <rect x="40" y="40" width="520" height="420" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#p3Grad)" />

  <!-- STANDARDIZED PROJECT ARTWORK PANEL -->
  <rect x="36" y="36" width="528" height="428" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g clip-path="url(#fmArtClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.68)">
      {ref7_inner}
    </g>
  </g>

  <!-- CONTENT PANEL -->
  <g transform="translate(600, 45)">
    <rect x="0" y="0" width="940" height="410" fill="#1A0A1F" stroke="#E86A33" stroke-width="2" rx="12" />

    <rect x="35" y="25" width="500" height="50" fill="#E86A33" rx="4" />
    <text x="55" y="60" font-family="'Impact', sans-serif" font-size="32" font-weight="900" fill="#F5F1E8" letter-spacing="3">UNIVERSE 03 // FORGEMIND</text>

    <g transform="translate(35, 95)">
      <text x="0" y="25" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#F5B041">"Every codebase is a universe. Someone has to understand it."</text>
      
      <g font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8" transform="translate(0, 50)">
        <text x="0" y="0">Open-Source Maintainer Copilot &amp; Contributor Mentor performing</text>
        <text x="0" y="25">repository graph search, issue triaging, and automated mentorship.</text>
      </g>

      <g transform="translate(0, 120)" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
        <circle cx="10" cy="0" r="4" fill="#E86A33" />
        <text x="25" y="4">Repository Graph Search &amp; Codebase Reasoning</text>

        <circle cx="10" cy="30" r="4" fill="#F5B041" />
        <text x="25" y="34">Automated Issue Triaging &amp; Contributor Mentorship</text>

        <circle cx="10" cy="60" r="4" fill="#F5F1E8" />
        <text x="25" y="64">Multi-Agent Codebase Collaboration</text>
      </g>

      <g transform="translate(0, 220)" font-family="'Courier New', monospace" font-size="12" fill="#F5F1E8">
        <rect x="0" y="0" width="110" height="30" fill="#2D112C" stroke="#E86A33" stroke-width="1.5" rx="3" />
        <text x="55" y="20" text-anchor="middle">LANGCHAIN</text>

        <rect x="125" y="0" width="130" height="30" fill="#2D112C" stroke="#F5B041" stroke-width="1.5" rx="3" />
        <text x="190" y="20" text-anchor="middle">FAISS</text>

        <rect x="270" y="0" width="130" height="30" fill="#2D112C" stroke="#F5F1E8" stroke-width="1.5" rx="3" />
        <text x="335" y="20" text-anchor="middle">GITHUB API</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/scenes/project-forgemind.svg', 'w', encoding='utf-8') as f:
    f.write(project_fm_content)
print("Clean project-forgemind.svg generated.")

# ==============================================================================
# 7. PROJECT 04: project-autohr.svg (Ref #8: download (6).svg)
# ==============================================================================
ref8_inner = extract_inner_svg('assets/reference/download (6).svg', 'ref8')

project_hr_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#1A0A1F" />
    </linearGradient>

    <clipPath id="hrArtClip">
      <rect x="40" y="40" width="520" height="420" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#p4Grad)" />

  <!-- STANDARDIZED PROJECT ARTWORK PANEL -->
  <rect x="36" y="36" width="528" height="428" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g clip-path="url(#hrArtClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.68)">
      {ref8_inner}
    </g>
  </g>

  <!-- CONTENT PANEL -->
  <g transform="translate(600, 45)">
    <rect x="0" y="0" width="940" height="410" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="12" />

    <rect x="35" y="25" width="460" height="50" fill="#F5B041" rx="4" />
    <text x="55" y="60" font-family="'Impact', sans-serif" font-size="32" font-weight="900" fill="#1A0A1F" letter-spacing="3">UNIVERSE 04 // AUTOHR</text>

    <g transform="translate(35, 95)">
      <text x="0" y="25" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#E86A33">"The best automation doesn't feel automated."</text>
      
      <g font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8" transform="translate(0, 50)">
        <text x="0" y="0">AI-Powered HR Workflow Automation &amp; Induction Narration System</text>
        <text x="0" y="25">automating meeting summaries, voice generation, and onboarding flows.</text>
      </g>

      <g transform="translate(0, 120)" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
        <circle cx="10" cy="0" r="4" fill="#F5B041" />
        <text x="25" y="4">Autonomous Meeting Summarization &amp; Action Extraction</text>

        <circle cx="10" cy="30" r="4" fill="#E86A33" />
        <text x="25" y="34">AI Voice Narration &amp; Presentation Control</text>

        <circle cx="10" cy="60" r="4" fill="#F5F1E8" />
        <text x="25" y="64">Teams &amp; Induction Workflow Orchestration</text>
      </g>

      <g transform="translate(0, 220)" font-family="'Courier New', monospace" font-size="12" fill="#F5F1E8">
        <rect x="0" y="0" width="110" height="30" fill="#54152B" stroke="#F5B041" stroke-width="1.5" rx="3" />
        <text x="55" y="20" text-anchor="middle">PYTHON</text>

        <rect x="125" y="0" width="130" height="30" fill="#54152B" stroke="#E86A33" stroke-width="1.5" rx="3" />
        <text x="190" y="20" text-anchor="middle">WHISPER</text>

        <rect x="270" y="0" width="130" height="30" fill="#54152B" stroke="#F5F1E8" stroke-width="1.5" rx="3" />
        <text x="335" y="20" text-anchor="middle">TTS VOICE</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/scenes/project-autohr.svg', 'w', encoding='utf-8') as f:
    f.write(project_hr_content)
print("Clean project-autohr.svg generated.")

# ==============================================================================
# 8. MISSION CONTROL: mission-control.svg (Ref #9: Bookmarks _ X.svg)
# ==============================================================================
ref9_inner = extract_inner_svg('assets/reference/Bookmarks _ X.svg', 'ref9')

mc_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 550" width="100%" height="100%">
  <defs>
    <linearGradient id="mcBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="60%" stop-color="#54152B" />
      <stop offset="100%" stop-color="#2D112C" />
    </linearGradient>

    <clipPath id="bookmarksClip">
      <rect x="40" y="40" width="500" height="460" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="550" fill="url(#mcBg)" />

  <!-- SECTION HEADER -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="280" height="40" fill="#E86A33" rx="4" />
    <text x="140" y="26" font-family="'Courier New', monospace" font-size="15" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">MISSION CONTROL</text>
  </g>

  <!-- LEFT ARTWORK PANEL -->
  <rect x="36" y="96" width="508" height="418" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g transform="translate(40, 100)">
    <g clip-path="url(#bookmarksClip)" opacity="0.95">
      <g transform="translate(0, -20) scale(0.68)">
        {ref9_inner}
      </g>
    </g>
  </g>

  <!-- RIGHT MISSION LOGS -->
  <g transform="translate(580, 100)">
    <rect x="0" y="0" width="940" height="410" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="12" />
    
    <text x="40" y="55" font-family="'Impact', sans-serif" font-size="28" fill="#F5B041" letter-spacing="2">ACTIVE MISSIONS &amp; BUILDING LOGS</text>
    <text x="40" y="85" font-family="'Courier New', monospace" font-size="14" fill="#E86A33" font-weight="900">STATUS: TRANSMISSION ACTIVE // EARTH-2705</text>

    <g transform="translate(40, 130)" font-family="'Courier New', monospace" font-size="15" fill="#F5F1E8">
      <g transform="translate(0, 0)">
        <text x="0" y="0" font-weight="900" fill="#F5B041">→ AGENTIC AI &amp; MULTI-AGENT ORCHESTRATION</text>
        <text x="25" y="25" fill="#D0C4DF">Building stateful execution graphs with long-term memory &amp; tool safety.</text>
      </g>

      <g transform="translate(0, 75)">
        <text x="0" y="0" font-weight="900" fill="#E86A33">→ HIGH-PERFORMANCE RAG &amp; VECTOR RETRIEVAL</text>
        <text x="25" y="25" fill="#D0C4DF">Optimizing hybrid dense search, reranking, and legal evidence parsing.</text>
      </g>

      <g transform="translate(0, 150)">
        <text x="0" y="0" font-weight="900" fill="#F5F1E8">→ PRODUCTION AI INFRASTRUCTURE</text>
        <text x="25" y="25" fill="#D0C4DF">Deploying scalable FastAPI microservices, Docker containers, and PGVector.</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/scenes/mission-control.svg', 'w', encoding='utf-8') as f:
    f.write(mc_content)
print("Clean mission-control.svg generated.")

# ==============================================================================
# 9. SCENE 08: scene08-ending.svg (Ref #10: download (3).svg, Char #5: atharva-running.svg)
# ==============================================================================
ref10_inner = extract_inner_svg('assets/reference/download (3).svg', 'ref10')
char5_inner = extract_inner_svg('assets/characters/atharva-running.svg', 'char5')

scene08_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 520" width="100%" height="100%">
  <defs>
    <linearGradient id="nightEnding" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="50%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#09040D" />
    </linearGradient>

    <clipPath id="endArtClip">
      <rect x="40" y="40" width="640" height="440" rx="10" />
    </clipPath>

    <style>
      @keyframes runMotion {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(30px, 0); }}
        100% {{ transform: translate(0, 0); }}
      }}
      .anim-run {{ animation: runMotion 3s ease-in-out infinite; }}
    </style>
  </defs>

  <rect width="1600" height="520" fill="url(#nightEnding)" />

  <!-- LEFT SIDE ARTWORK PANEL (42% WIDTH WITH NATURAL PROPORTION) -->
  <rect x="36" y="36" width="648" height="448" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g clip-path="url(#endArtClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.82)">
      {ref10_inner}
    </g>
  </g>

  <!-- FOREGROUND RUNNING CHARACTER OVERLAPPING PANEL -->
  <g transform="translate(540, 90)" class="anim-run">
    <g transform="scale(0.58)">
      {char5_inner}
    </g>
  </g>

  <!-- RIGHT CINEMATIC ENDING TEXT PANEL -->
  <g transform="translate(860, 100)">
    <rect x="0" y="0" width="680" height="320" fill="#1A0A1F" opacity="0.95" stroke="#F5B041" stroke-width="2" rx="10" />
    
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
print("Clean scene08-ending.svg generated.")
