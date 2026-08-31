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
# BUILD SCENE 01: scene01-cover.svg
# Ref Asset #1: Across The Spider-Verse Wallpaper.svg
# Character #1: atharva-hero.svg
# ==============================================================================
ref1_inner = extract_inner_svg('assets/reference/Across The Spider-Verse Wallpaper.svg', 'ref1')
char1_inner = extract_inner_svg('assets/characters/atharva-hero.svg', 'char1')

scene01_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 850" width="100%" height="100%">
  <defs>
    <linearGradient id="coverSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="35%" stop-color="#54152B" />
      <stop offset="70%" stop-color="#B83228" />
      <stop offset="100%" stop-color="#E86A33" />
    </linearGradient>

    <radialGradient id="sunBurst" cx="50%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#F5B041" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#E86A33" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#1A0A1F" stop-opacity="0" />
    </radialGradient>

    <pattern id="coverHalftone" x="0" y="0" width="10" height="10" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.5" fill="#F5B041" fill-opacity="0.3" />
    </pattern>

    <clipPath id="heroArtworkClip">
      <polygon points="650,40 1600,40 1600,810 650,810" />
    </clipPath>
  </defs>

  <!-- LAYER 0: BACKGROUND GRADIENT & SUNSET ATMOSPHERE -->
  <rect width="1600" height="850" fill="url(#coverSky)" />
  <rect width="1600" height="850" fill="url(#sunBurst)" />
  <rect width="1600" height="850" fill="url(#coverHalftone)" />

  <!-- LAYER 1: INLINED FOREGROUND REFERENCE ARTWORK #1 (Across The Spider-Verse Wallpaper.svg) -->
  <g clip-path="url(#heroArtworkClip)" opacity="0.92">
    <g transform="translate(600, -80) scale(1.1)">
      {ref1_inner}
    </g>
  </g>

  <!-- LAYER 2: INLINED FOREGROUND ATHARVA HERO CHARACTER #1 (atharva-hero.svg) -->
  <g transform="translate(1000, 180) scale(0.95)">
    {char1_inner}
  </g>

  <!-- LAYER 3: COMIC ISSUE HEADER BADGE -->
  <g transform="translate(80, 50)">
    <polygon points="0,0 420,0 400,46 0,46" fill="#E86A33" stroke="#F5F1E8" stroke-width="2" />
    <text x="200" y="30" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">ISSUE #01 // ATHARVA'S UNIVERSE</text>
  </g>

  <!-- LAYER 4: HUGE MULTIVERSE COMIC TYPOGRAPHY -->
  <g transform="translate(80, 280) skewX(-10)">
    <text x="12" y="12" font-family="'Impact', 'Arial Black', sans-serif" font-size="140" font-weight="900" letter-spacing="12" fill="#1A0A1F">ATHARVA</text>
    <text x="-6" y="-6" font-family="'Impact', 'Arial Black', sans-serif" font-size="140" font-weight="900" letter-spacing="12" fill="#F5B041">ATHARVA</text>
    <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="140" font-weight="900" letter-spacing="12" fill="#F5F1E8">ATHARVA</text>

    <text x="12" y="152" font-family="'Impact', 'Arial Black', sans-serif" font-size="140" font-weight="900" letter-spacing="12" fill="#1A0A1F">PATHAK</text>
    <text x="-6" y="134" font-family="'Impact', 'Arial Black', sans-serif" font-size="140" font-weight="900" letter-spacing="12" fill="#F5B041">PATHAK</text>
    <text x="0" y="140" font-family="'Impact', 'Arial Black', sans-serif" font-size="140" font-weight="900" letter-spacing="12" fill="#F5F1E8">PATHAK</text>
  </g>

  <!-- LAYER 5: SUBTITLE BANNER & NARRATIVE CAPTION -->
  <g transform="translate(80, 540) rotate(-2)">
    <polygon points="0,0 520,0 500,60 0,60" fill="#F5B041" stroke="#1A0A1F" stroke-width="4" />
    <text x="250" y="40" font-family="'Impact', sans-serif" font-size="34" font-weight="900" letter-spacing="4" text-anchor="middle" fill="#1A0A1F">★ AI ENGINEER ★</text>
  </g>

  <g transform="translate(80, 650)">
    <polygon points="0,0 780,0 750,80 0,80" fill="#1A0A1F" stroke="#F5F1E8" stroke-width="3" />
    <text x="30" y="35" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#F5B041">"BUILDING SYSTEMS THAT REMEMBER, REASON &amp; ACT."</text>
    <text x="30" y="60" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8" font-style="italic">With great curiosity comes great responsibility.</text>
  </g>
</svg>'''

with open('assets/scenes/scene01-cover.svg', 'w', encoding='utf-8') as f:
    f.write(scene01_content)
print("scene01-cover.svg built successfully.")

# ==============================================================================
# BUILD SCENE 02: scene02-strip.svg
# Ref Asset #2: Spider Man Into The Spider Verse Poster.svg
# Character #2: atharva-swing.svg
# ==============================================================================
ref2_inner = extract_inner_svg('assets/reference/Spider Man Into The Spider Verse Poster.svg', 'ref2')
char2_inner = extract_inner_svg('assets/characters/atharva-swing.svg', 'char2')

scene02_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 450" width="100%" height="100%">
  <defs>
    <linearGradient id="stripSky" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E86A33" />
      <stop offset="50%" stop-color="#B83228" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="posterClip">
      <polygon points="40,20 580,20 540,420 40,420" />
    </clipPath>

    <style>
      @keyframes swingMove {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(30px, -15px); }}
        100% {{ transform: translate(0, 0); }}
      }}
      .anim-swing {{ animation: swingMove 4s ease-in-out infinite; }}
    </style>
  </defs>

  <!-- LAYER 0: BACKGROUND GRADIENT -->
  <rect width="1600" height="450" fill="url(#stripSky)" />

  <!-- LAYER 1: INLINED FOREGROUND REFERENCE ARTWORK #2 (Spider Man Into The Spider Verse Poster.svg) -->
  <g clip-path="url(#posterClip)" opacity="0.92">
    <g transform="translate(40, -40) scale(0.7)">
      {ref2_inner}
    </g>
  </g>

  <!-- LAYER 2: INLINED FOREGROUND ATHARVA SWING CHARACTER #2 (atharva-swing.svg) -->
  <g transform="translate(560, 40)" class="anim-swing">
    <g transform="scale(0.55)">
      {char2_inner}
    </g>
  </g>

  <!-- LAYER 3: SWINGING KINETIC WEB TRAJECTORY -->
  <path d="M 750,180 Q 1100,320 1550,120" stroke="#F5B041" stroke-width="5" stroke-dasharray="12,6" fill="none" />

  <!-- LAYER 4: COMIC NARRATION CAPTION BOX -->
  <g transform="translate(900, 100)">
    <polygon points="0,0 640,0 600,260 0,260" fill="#1A0A1F" stroke="#F5B041" stroke-width="3" />
    
    <text x="40" y="50" font-family="'Impact', sans-serif" font-size="28" fill="#F5B041" letter-spacing="2">EVERY UNIVERSE STARTS WITH CURIOSITY.</text>

    <g font-family="'Courier New', monospace" font-size="15" fill="#F5F1E8">
      <text x="40" y="100">Mine started with a question:</text>
      <text x="40" y="135" font-weight="700" fill="#F5B041">"What if machines could retrieve knowledge, reason over context,</text>
      <text x="40" y="165" font-weight="700" fill="#E86A33">and safely act in real-world workflows?"</text>
      <text x="40" y="215" fill="#D0C4DF">A question became an experiment. Experiments became systems.</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene02-strip.svg', 'w', encoding='utf-8') as f:
    f.write(scene02_content)
print("scene02-strip.svg built successfully.")

# ==============================================================================
# BUILD SCENE 03: scene03-rooftop.svg
# Ref Asset #3: Spider-Man Homecoming PNG.svg
# Character #3: atharva-rooftop.svg
# ==============================================================================
ref3_inner = extract_inner_svg('assets/reference/Spider-Man_ Homecoming Film Series Marvel Cinematic Universe Spider-Man_ Homecoming Film Series Marvel Studios PNG.svg', 'ref3')
char3_inner = extract_inner_svg('assets/characters/atharva-rooftop.svg', 'char3')

scene03_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="rooftopSunset" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#54152B" />
      <stop offset="60%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#1A0A1F" />
    </linearGradient>

    <clipPath id="homecomingClip">
      <polygon points="40,20 480,20 440,460 40,460" />
    </clipPath>
  </defs>

  <!-- LAYER 0: BACKGROUND GRADIENT -->
  <rect width="1600" height="500" fill="url(#rooftopSunset)" />

  <!-- LAYER 1: INLINED FOREGROUND REFERENCE ARTWORK #3 (Spider-Man Homecoming PNG.svg) -->
  <g clip-path="url(#homecomingClip)" opacity="0.95">
    <g transform="translate(40, 20) scale(0.8)">
      {ref3_inner}
    </g>
  </g>

  <!-- LAYER 2: INLINED FOREGROUND ATHARVA ROOFTOP CHARACTER #3 (atharva-rooftop.svg) -->
  <g transform="translate(480, 80)">
    <g transform="scale(0.55)">
      {char3_inner}
    </g>
  </g>

  <!-- LAYER 3: RIGHT CINEMATIC ROOFTOP PHILOSOPHY CARD -->
  <g transform="translate(860, 80)">
    <polygon points="0,0 680,0 640,340 0,340" fill="#1A0A1F" stroke="#F5B041" stroke-width="3" />
    
    <text x="40" y="55" font-family="'Impact', sans-serif" font-size="32" fill="#F5B041" letter-spacing="2">THE ROOFTOP PERSPECTIVE</text>

    <g font-family="'Courier New', monospace" font-size="16" fill="#F5F1E8">
      <text x="40" y="115" font-weight="900" fill="#E86A33">"Every engineer sees a problem."</text>
      <text x="40" y="145" font-weight="900" fill="#F5B041">"I see a living system waiting to be understood."</text>

      <text x="40" y="210" fill="#F5F1E8">DESIGNATION: AI ENGINEER</text>
      <text x="40" y="240" fill="#F5F1E8">FOCUS: LLMs • RAG • AGENTIC SYSTEMS • LANGGRAPH</text>
      <text x="40" y="270" fill="#D0C4DF">LOCATION: EARTH-2705 // ONLINE</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene03-rooftop.svg', 'w', encoding='utf-8') as f:
    f.write(scene03_content)
print("scene03-rooftop.svg built successfully.")

# ==============================================================================
# BUILD SCENE 05: scene05-leap.svg
# Ref Asset #4: Spider Man_ Across The Spider Verse Wallpaper.svg
# Character #4: atharva-leap.svg
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
      <polygon points="40,20 680,20 640,510 40,510" />
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

  <!-- LAYER 0: BACKGROUND GRADIENT -->
  <rect width="1600" height="550" fill="url(#leapBg)" />

  <!-- LAYER 1: INLINED FOREGROUND REFERENCE ARTWORK #4 (Spider Man_ Across The Spider Verse Wallpaper.svg) -->
  <g clip-path="url(#leapRefClip)" opacity="0.95">
    <g transform="translate(40, -50) scale(0.8)">
      {ref4_inner}
    </g>
  </g>

  <!-- LAYER 2: INLINED FOREGROUND ATHARVA LEAP CHARACTER #4 (atharva-leap.svg) -->
  <g transform="translate(680, 50)" class="anim-leap">
    <g transform="scale(0.6)">
      {char4_inner}
    </g>
  </g>

  <!-- LAYER 3: KINETIC DYNAMIC TRAJECTORY -->
  <path d="M 980,260 Q 1250,380 1550,220" stroke="#F5B041" stroke-width="6" stroke-dasharray="12,6" fill="none" />

  <!-- LAYER 4: RIGHT PORTAL INTRODUCTION NARRATIVE -->
  <g transform="translate(1080, 90)">
    <polygon points="0,0 480,0 440,360 0,360" fill="#1A0A1F" stroke="#F5B041" stroke-width="3" />
    
    <text x="35" y="60" font-family="'Impact', sans-serif" font-size="30" fill="#F5B041" letter-spacing="2">ENTER THE MULTIVERSE</text>
    <text x="35" y="95" font-family="'Courier New', monospace" font-size="15" fill="#E86A33" font-weight="900">// PROJECT UNIVERSES</text>

    <g font-family="'Courier New', monospace" font-size="15" fill="#F5F1E8">
      <text x="35" y="160">Every project is a distinct</text>
      <text x="35" y="190" font-weight="900" fill="#F5B041">multiverse dimension with its</text>
      <text x="35" y="220" font-weight="900" fill="#E86A33">own architectural story.</text>
      
      <text x="35" y="290" font-size="14" fill="#D0C4DF">LEAPING IN →</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene05-leap.svg', 'w', encoding='utf-8') as f:
    f.write(scene05_content)
print("scene05-leap.svg built successfully.")

# ==============================================================================
# BUILD PROJECT 01: project-meravyapar.svg
# Ref Asset #5: download (4).svg
# ==============================================================================
ref5_inner = extract_inner_svg('assets/reference/download (4).svg', 'ref5')

project_mv_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="mvArtClip">
      <polygon points="20,20 540,20 500,320 20,320" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#p1Grad)" />

  <g transform="translate(40, 40)">
    <polygon points="0,0 1520,0 1460,420 0,420" fill="#1A0A1F" stroke="#E86A33" stroke-width="4" />

    <!-- UNIVERSE TITLE -->
    <polygon points="40,25 580,25 560,85 40,85" fill="#E86A33" stroke="#F5F1E8" stroke-width="2" />
    <text x="65" y="65" font-family="'Impact', sans-serif" font-size="34" font-weight="900" fill="#F5F1E8" letter-spacing="3">UNIVERSE 01 // MERAVYAPAR AI</text>

    <!-- INLINED FOREGROUND REFERENCE ARTWORK #5 (download (4).svg) -->
    <g transform="translate(40, 100)">
      <g clip-path="url(#mvArtClip)" opacity="0.95">
        <g transform="translate(0, -20) scale(0.7)">
          {ref5_inner}
        </g>
      </g>
    </g>

    <!-- NARRATIVE TAGLINE & DESCRIPTION -->
    <g transform="translate(620, 110)">
      <text x="0" y="25" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#F5B041">"Money leaves clues. Intelligent systems learn to follow them."</text>
      
      <g font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8" transform="translate(0, 50)">
        <text x="0" y="0">AI Financial Autopilot for merchants parsing fragmented transactions,</text>
        <text x="0" y="25">evidence-driven reconciliation, receivables prioritization, and payment promises.</text>
      </g>

      <!-- FEATURE LIST -->
      <g transform="translate(0, 120)" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
        <circle cx="10" cy="0" r="4" fill="#E86A33" />
        <text x="25" y="4">Financial Intelligence Graph &amp; Transaction Evidence</text>

        <circle cx="10" cy="30" r="4" fill="#F5B041" />
        <text x="25" y="34">Receivables Prioritization &amp; Payment Promise Tracking</text>

        <circle cx="10" cy="60" r="4" fill="#F5F1E8" />
        <text x="25" y="64">Agentic Financial Analysis Pipeline</text>
      </g>

      <!-- TECH TAG BADGES -->
      <g transform="translate(0, 220)" font-family="'Courier New', monospace" font-size="12" fill="#F5F1E8">
        <rect x="0" y="0" width="110" height="30" fill="#2D112C" stroke="#E86A33" stroke-width="1.5" />
        <text x="55" y="20" text-anchor="middle">FASTAPI</text>

        <rect x="125" y="0" width="130" height="30" fill="#2D112C" stroke="#F5B041" stroke-width="1.5" />
        <text x="190" y="20" text-anchor="middle">LANGGRAPH</text>

        <rect x="270" y="0" width="130" height="30" fill="#2D112C" stroke="#F5F1E8" stroke-width="1.5" />
        <text x="335" y="20" text-anchor="middle">POSTGRESQL</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/scenes/project-meravyapar.svg', 'w', encoding='utf-8') as f:
    f.write(project_mv_content)
print("project-meravyapar.svg built successfully.")

# ==============================================================================
# BUILD PROJECT 03: project-forgemind.svg
# Ref Asset #7: download (5).svg
# ==============================================================================
ref7_inner = extract_inner_svg('assets/reference/download (5).svg', 'ref7')

project_fm_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="fmArtClip">
      <polygon points="20,20 540,20 500,320 20,320" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#p3Grad)" />

  <g transform="translate(40, 40)">
    <polygon points="0,0 1520,0 1480,420 0,420" fill="#1A0A1F" stroke="#E86A33" stroke-width="4" />

    <!-- UNIVERSE TITLE -->
    <polygon points="40,25 540,25 520,85 40,85" fill="#E86A33" stroke="#F5F1E8" stroke-width="2" />
    <text x="65" y="65" font-family="'Impact', sans-serif" font-size="34" font-weight="900" fill="#F5F1E8" letter-spacing="3">UNIVERSE 03 // FORGEMIND</text>

    <!-- INLINED FOREGROUND REFERENCE ARTWORK #7 (download (5).svg) -->
    <g transform="translate(40, 100)">
      <g clip-path="url(#fmArtClip)" opacity="0.95">
        <g transform="translate(0, -20) scale(0.65)">
          {ref7_inner}
        </g>
      </g>
    </g>

    <!-- NARRATIVE DESCRIPTION -->
    <g transform="translate(620, 110)">
      <text x="0" y="25" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#F5B041">"Every codebase is a universe. Someone has to understand it."</text>
      
      <g font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8" transform="translate(0, 50)">
        <text x="0" y="0">Open-Source Maintainer Copilot &amp; Contributor Mentor performing</text>
        <text x="0" y="25">repository graph search, issue triaging, and automated mentorship.</text>
      </g>

      <!-- FEATURE LIST -->
      <g transform="translate(0, 120)" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
        <circle cx="10" cy="0" r="4" fill="#E86A33" />
        <text x="25" y="4">Repository Graph Search &amp; Codebase Reasoning</text>

        <circle cx="10" cy="30" r="4" fill="#F5B041" />
        <text x="25" y="34">Automated Issue Triaging &amp; Contributor Mentorship</text>

        <circle cx="10" cy="60" r="4" fill="#F5F1E8" />
        <text x="25" y="64">Multi-Agent Codebase Collaboration</text>
      </g>

      <!-- TECH TAG BADGES -->
      <g transform="translate(0, 220)" font-family="'Courier New', monospace" font-size="12" fill="#F5F1E8">
        <rect x="0" y="0" width="110" height="30" fill="#2D112C" stroke="#E86A33" stroke-width="1.5" />
        <text x="55" y="20" text-anchor="middle">LANGCHAIN</text>

        <rect x="125" y="0" width="130" height="30" fill="#2D112C" stroke="#F5B041" stroke-width="1.5" />
        <text x="190" y="20" text-anchor="middle">FAISS</text>

        <rect x="270" y="0" width="130" height="30" fill="#2D112C" stroke="#F5F1E8" stroke-width="1.5" />
        <text x="335" y="20" text-anchor="middle">GITHUB API</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/scenes/project-forgemind.svg', 'w', encoding='utf-8') as f:
    f.write(project_fm_content)
print("project-forgemind.svg built successfully.")

# ==============================================================================
# BUILD PROJECT 04: project-autohr.svg
# Ref Asset #8: download (6).svg
# ==============================================================================
ref8_inner = extract_inner_svg('assets/reference/download (6).svg', 'ref8')

project_hr_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#1A0A1F" />
    </linearGradient>

    <clipPath id="hrArtClip">
      <polygon points="20,20 540,20 500,320 20,320" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#p4Grad)" />

  <g transform="translate(40, 40)">
    <polygon points="0,0 1520,0 1480,420 0,420" fill="#1A0A1F" stroke="#F5B041" stroke-width="4" />

    <!-- UNIVERSE TITLE -->
    <polygon points="40,25 480,25 460,85 40,85" fill="#F5B041" stroke="#1A0A1F" stroke-width="2" />
    <text x="65" y="65" font-family="'Impact', sans-serif" font-size="34" font-weight="900" fill="#1A0A1F" letter-spacing="3">UNIVERSE 04 // AUTOHR</text>

    <!-- INLINED FOREGROUND REFERENCE ARTWORK #8 (download (6).svg) -->
    <g transform="translate(40, 100)">
      <g clip-path="url(#hrArtClip)" opacity="0.95">
        <g transform="translate(0, -20) scale(0.65)">
          {ref8_inner}
        </g>
      </g>
    </g>

    <!-- NARRATIVE DESCRIPTION -->
    <g transform="translate(620, 110)">
      <text x="0" y="25" font-family="'Courier New', monospace" font-size="16" font-weight="900" fill="#E86A33">"The best automation doesn't feel automated."</text>
      
      <g font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8" transform="translate(0, 50)">
        <text x="0" y="0">AI-Powered HR Workflow Automation &amp; Induction Narration System</text>
        <text x="0" y="25">automating meeting summaries, voice generation, and onboarding flows.</text>
      </g>

      <!-- FEATURE LIST -->
      <g transform="translate(0, 120)" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
        <circle cx="10" cy="0" r="4" fill="#F5B041" />
        <text x="25" y="4">Autonomous Meeting Summarization &amp; Action Extraction</text>

        <circle cx="10" cy="30" r="4" fill="#E86A33" />
        <text x="25" y="34">AI Voice Narration &amp; Presentation Control</text>

        <circle cx="10" cy="60" r="4" fill="#F5F1E8" />
        <text x="25" y="64">Teams &amp; Induction Workflow Orchestration</text>
      </g>

      <!-- TECH TAG BADGES -->
      <g transform="translate(0, 220)" font-family="'Courier New', monospace" font-size="12" fill="#F5F1E8">
        <rect x="0" y="0" width="110" height="30" fill="#54152B" stroke="#F5B041" stroke-width="1.5" />
        <text x="55" y="20" text-anchor="middle">PYTHON</text>

        <rect x="125" y="0" width="130" height="30" fill="#54152B" stroke="#E86A33" stroke-width="1.5" />
        <text x="190" y="20" text-anchor="middle">WHISPER</text>

        <rect x="270" y="0" width="130" height="30" fill="#54152B" stroke="#F5F1E8" stroke-width="1.5" />
        <text x="335" y="20" text-anchor="middle">TTS VOICE</text>
      </g>
    </g>
  </g>
</svg>'''

with open('assets/scenes/project-autohr.svg', 'w', encoding='utf-8') as f:
    f.write(project_hr_content)
print("project-autohr.svg built successfully.")

# ==============================================================================
# BUILD MISSION CONTROL: mission-control.svg
# Ref Asset #9: Bookmarks _ X.svg
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
      <polygon points="20,20 480,20 450,340 20,340" />
    </clipPath>
  </defs>

  <rect width="1600" height="550" fill="url(#mcBg)" />
  <rect x="20" y="20" width="1560" height="510" fill="none" stroke="#F5F1E8" stroke-width="4" />

  <!-- SECTION HEADER -->
  <g transform="translate(60, 45)">
    <polygon points="0,0 280,0 260,40 0,40" fill="#E86A33" stroke="#F5F1E8" stroke-width="2" />
    <text x="140" y="26" font-family="'Courier New', monospace" font-size="15" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">MISSION CONTROL</text>
  </g>

  <!-- INLINED FOREGROUND REFERENCE ARTWORK #9 (Bookmarks _ X.svg) -->
  <g transform="translate(60, 100)">
    <g clip-path="url(#bookmarksClip)" opacity="0.95">
      <g transform="translate(0, -20) scale(0.65)">
        {ref9_inner}
      </g>
    </g>
  </g>

  <!-- RIGHT MISSION LOGS & ACTIVE EXPLORATIONS -->
  <g transform="translate(580, 100)">
    <polygon points="0,0 920,0 880,380 0,380" fill="#1A0A1F" stroke="#F5B041" stroke-width="3" />
    
    <text x="40" y="50" font-family="'Impact', sans-serif" font-size="28" fill="#F5B041" letter-spacing="2">ACTIVE MISSIONS &amp; BUILDING LOGS</text>
    <text x="40" y="80" font-family="'Courier New', monospace" font-size="14" fill="#E86A33" font-weight="900">STATUS: TRANSMISSION ACTIVE // EARTH-2705</text>

    <!-- MISSION ITEMS -->
    <g transform="translate(40, 120)" font-family="'Courier New', monospace" font-size="15" fill="#F5F1E8">
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
print("mission-control.svg built successfully.")

# ==============================================================================
# BUILD MULTIVERSE CITY: multiverse-city.svg
# Ref Asset #6: MUMBATTAN.svg
# ==============================================================================
ref6_inner = extract_inner_svg('assets/reference/MUMBATTAN.svg', 'ref6')

city_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="cityDistrictBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="35%" stop-color="#54152B" />
      <stop offset="65%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#E86A33" />
    </linearGradient>

    <clipPath id="mumbattanClip">
      <rect x="0" y="0" width="1520" height="460" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#cityDistrictBg)" />
  
  <!-- INLINED FOREGROUND REFERENCE ARTWORK #6 (MUMBATTAN.svg AT 90% OPACITY) -->
  <g transform="translate(40, 20)" opacity="0.9" clip-path="url(#mumbattanClip)">
    <g transform="translate(0, -60) scale(0.8)">
      {ref6_inner}
    </g>
  </g>

  <rect x="20" y="20" width="1560" height="460" fill="none" stroke="#F5F1E8" stroke-width="4" />

  <!-- SECTION HEADER -->
  <g transform="translate(60, 45)">
    <polygon points="0,0 380,0 360,40 0,40" fill="#E86A33" stroke="#F5F1E8" stroke-width="2" />
    <text x="190" y="26" font-family="'Courier New', monospace" font-size="15" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">MULTIVERSE CITY // DISTRICTS</text>
  </g>

  <!-- FOUR PROJECT DISTRICT OVERLAYS -->
  <g transform="translate(60, 110)">
    <rect x="0" y="0" width="340" height="340" fill="#1A0A1F" opacity="0.9" stroke="#E86A33" stroke-width="3" />
    <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#E86A33" letter-spacing="1">FINANCIAL DISTRICT</text>
    <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#F5B041">// MeraVyapar AI</text>
    <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Fragmented transaction signals</text>
    <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">&amp; evidence graph engine.</text>
    <circle cx="280" cy="260" r="40" fill="none" stroke="#E86A33" stroke-width="2" stroke-dasharray="4,2" />
  </g>

  <g transform="translate(430, 110)">
    <rect x="0" y="0" width="340" height="340" fill="#1A0A1F" opacity="0.9" stroke="#F5B041" stroke-width="3" />
    <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#F5B041" letter-spacing="1">DOCUMENT DISTRICT</text>
    <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#E86A33">// BhoomiFlow</text>
    <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Land case evidence integrity</text>
    <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">&amp; legal document RAG.</text>
    <circle cx="280" cy="260" r="40" fill="none" stroke="#F5B041" stroke-width="2" stroke-dasharray="4,2" />
  </g>

  <g transform="translate(800, 110)">
    <rect x="0" y="0" width="340" height="340" fill="#1A0A1F" opacity="0.9" stroke="#54152B" stroke-width="3" />
    <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#F5F1E8" letter-spacing="1">CODEBASE DISTRICT</text>
    <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#F5B041">// ForgeMind</text>
    <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Repository intelligence &amp; issue</text>
    <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">triaging copilot.</text>
    <circle cx="280" cy="260" r="40" fill="none" stroke="#54152B" stroke-width="2" stroke-dasharray="4,2" />
  </g>

  <g transform="translate(1170, 110)">
    <rect x="0" y="0" width="340" height="340" fill="#1A0A1F" opacity="0.9" stroke="#E86A33" stroke-width="3" />
    <text x="20" y="40" font-family="'Impact', sans-serif" font-size="24" fill="#E86A33" letter-spacing="1">AUTOMATION DISTRICT</text>
    <text x="20" y="65" font-family="'Courier New', monospace" font-size="14" fill="#F5B041">// AutoHR</text>
    <text x="20" y="110" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">Automated meeting workflows</text>
    <text x="20" y="130" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">&amp; induction narration.</text>
    <circle cx="280" cy="260" r="40" fill="none" stroke="#E86A33" stroke-width="2" stroke-dasharray="4,2" />
  </g>

  <path d="M 100,200 Q 800,450 1500,200" fill="none" stroke="#F5B041" stroke-width="3" stroke-dasharray="8,4" opacity="0.85" />
</svg>'''

with open('assets/scenes/multiverse-city.svg', 'w', encoding='utf-8') as f:
    f.write(city_content)
print("multiverse-city.svg built successfully.")

# ==============================================================================
# BUILD SCENE 08: scene08-ending.svg
# Ref Asset #10: download (3).svg
# Character #5: atharva-running.svg
# ==============================================================================
ref10_inner = extract_inner_svg('assets/reference/download (3).svg', 'ref10')
char5_inner = extract_inner_svg('assets/characters/atharva-running.svg', 'char5')

scene08_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 450" width="100%" height="100%">
  <defs>
    <linearGradient id="nightEnding" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="50%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#09040D" />
    </linearGradient>

    <clipPath id="endArtClip">
      <polygon points="20,20 480,20 450,340 20,340" />
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

  <rect width="1600" height="450" fill="url(#nightEnding)" />

  <!-- INLINED FOREGROUND REFERENCE ARTWORK #10 (download (3).svg) -->
  <g transform="translate(60, 60)">
    <g clip-path="url(#endArtClip)" opacity="0.95">
      <g transform="translate(0, -20) scale(0.65)">
        {ref10_inner}
      </g>
    </g>
  </g>

  <!-- INLINED FOREGROUND ATHARVA RUNNING CHARACTER #5 (atharva-running.svg) -->
  <g transform="translate(540, 80)" class="anim-run">
    <g transform="scale(0.55)">
      {char5_inner}
    </g>
  </g>

  <!-- CINEMATIC ENDING TEXT OVERLAY -->
  <g transform="translate(880, 120)">
    <polygon points="0,0 660,0 620,220 0,220" fill="#1A0A1F" opacity="0.95" stroke="#F5B041" stroke-width="3" />
    <text x="40" y="55" font-family="'Courier New', monospace" font-size="20" font-weight="900" fill="#F5B041">"Some systems answer questions."</text>
    <text x="40" y="95" font-family="'Impact', sans-serif" font-size="24" font-weight="900" fill="#F5F1E8" letter-spacing="2">"I WANT TO BUILD THE ONES THAT CHANGE WHAT HAPPENS NEXT."</text>

    <g transform="translate(40, 140)">
      <polygon points="0,0 260,0 240,45 0,45" fill="#E86A33" stroke="#1A0A1F" stroke-width="2" />
      <text x="120" y="30" font-family="'Impact', sans-serif" font-size="22" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">TO BE CONTINUED...</text>
    </g>
  </g>
</svg>'''

with open('assets/scenes/scene08-ending.svg', 'w', encoding='utf-8') as f:
    f.write(scene08_content)
print("scene08-ending.svg built successfully.")
