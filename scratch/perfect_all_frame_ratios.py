import os
import re

def extract_inner_svg(file_path, prefix=""):
    if not os.path.exists(file_path):
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
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

# 1. SCENE 02: 683x1024 (0.666992). Frame: 266.8 x 400.0 (0.6670)
ref2_inner = extract_inner_svg('assets/reference/Spider Man Into The Spider Verse Poster.svg', 'ref2')
scene02_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 480" width="100%" height="100%">
  <defs>
    <linearGradient id="stripSky" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E86A33" />
      <stop offset="50%" stop-color="#B83228" />
      <stop offset="100%" stop-color="#54152B" />
    </linearGradient>

    <clipPath id="posterClip">
      <rect x="40" y="40" width="266.8" height="400" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="480" fill="url(#stripSky)" />

  <rect x="36" y="36" width="274.8" height="408" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#posterClip)" opacity="0.95">
    <g transform="translate(40, 40) scale(0.390625)">
      {ref2_inner}
    </g>
  </g>

  <g transform="translate(360, 80)">
    <rect x="0" y="0" width="1180" height="320" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
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

# 2. SCENE 05: 736x331 (2.223565). Frame: 1045.07 x 470.0 (2.2236)
ref4_inner = extract_inner_svg('assets/reference/Spider Man_ Across The Spider Verse Wallpaper.svg', 'ref4')
scene05_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 550" width="100%" height="100%">
  <defs>
    <linearGradient id="leapBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="50%" stop-color="#54152B" />
      <stop offset="100%" stop-color="#B83228" />
    </linearGradient>

    <clipPath id="leapRefClip">
      <rect x="40" y="40" width="1045.07" height="470" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="550" fill="url(#leapBg)" />

  <rect x="36" y="36" width="1053.07" height="478" fill="#1A0A1F" rx="12" stroke="#F5B041" stroke-width="2" />
  <g clip-path="url(#leapRefClip)" opacity="0.95">
    <g transform="translate(40, 40) scale(1.419932)">
      {ref4_inner}
    </g>
  </g>

  <g transform="translate(1120, 90)">
    <rect x="0" y="0" width="440" height="370" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="10" />
    <text x="35" y="60" font-family="'Impact', sans-serif" font-size="28" fill="#F5B041" letter-spacing="2">ENTER THE MULTIVERSE</text>
    <text x="35" y="95" font-family="'Courier New', monospace" font-size="14" fill="#E86A33" font-weight="900">// PROJECT UNIVERSES</text>

    <g font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
      <text x="35" y="160">Every project is a distinct</text>
      <text x="35" y="190" font-weight="900" fill="#F5B041">multiverse dimension with its</text>
      <text x="35" y="220" font-weight="900" fill="#E86A33">own architectural story.</text>
      <text x="35" y="295" font-size="13" fill="#D0C4DF">LEAPING IN →</text>
    </g>
  </g>
</svg>'''
with open('assets/scenes/scene05-leap.svg', 'w', encoding='utf-8') as f:
    f.write(scene05_content)

# 3. PROJECT AUTOHR: 735x324 (2.2685185). Frame: 952.78 x 420.0 (2.2685)
ref8_inner = extract_inner_svg('assets/reference/download (6).svg', 'ref8')
project_hr_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2D112C" />
      <stop offset="100%" stop-color="#1A0A1F" />
    </linearGradient>

    <clipPath id="hrArtClip">
      <rect x="40" y="40" width="952.78" height="420" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="500" fill="url(#p4Grad)" />

  <rect x="36" y="36" width="960.78" height="428" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g clip-path="url(#hrArtClip)" opacity="0.95">
    <g transform="translate(40, 40) scale(1.296296)">
      {ref8_inner}
    </g>
  </g>

  <g transform="translate(1030, 45)">
    <rect x="0" y="0" width="510" height="410" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="12" />

    <rect x="25" y="25" width="460" height="50" fill="#F5B041" rx="4" />
    <text x="45" y="60" font-family="'Impact', sans-serif" font-size="28" font-weight="900" fill="#1A0A1F" letter-spacing="2">UNIVERSE 04 // AUTOHR</text>

    <g transform="translate(25, 95)">
      <text x="0" y="25" font-family="'Courier New', monospace" font-size="14" font-weight="900" fill="#E86A33">"Automation shouldn't feel automated."</text>
      
      <g font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8" transform="translate(0, 50)">
        <text x="0" y="0">AI-Powered HR Workflow Automation &amp;</text>
        <text x="0" y="22">Induction Narration System automating</text>
        <text x="0" y="44">meeting summaries &amp; onboarding.</text>
      </g>

      <g transform="translate(0, 130)" font-family="'Courier New', monospace" font-size="13" fill="#F5F1E8">
        <circle cx="10" cy="0" r="4" fill="#F5B041" />
        <text x="25" y="4">Autonomous Meeting Summaries</text>

        <circle cx="10" cy="25" r="4" fill="#E86A33" />
        <text x="25" y="29">AI Voice Narration Control</text>

        <circle cx="10" cy="50" r="4" fill="#F5F1E8" />
        <text x="25" y="54">Induction Orchestration</text>
      </g>

      <g transform="translate(0, 220)" font-family="'Courier New', monospace" font-size="11" fill="#F5F1E8">
        <rect x="0" y="0" width="90" height="28" fill="#54152B" stroke="#F5B041" stroke-width="1.5" rx="3" />
        <text x="45" y="18" text-anchor="middle">PYTHON</text>

        <rect x="105" y="0" width="100" height="28" fill="#54152B" stroke="#E86A33" stroke-width="1.5" rx="3" />
        <text x="155" y="18" text-anchor="middle">WHISPER</text>

        <rect x="220" y="0" width="100" height="28" fill="#54152B" stroke="#F5F1E8" stroke-width="1.5" rx="3" />
        <text x="270" y="18" text-anchor="middle">TTS VOICE</text>
      </g>
    </g>
  </g>
</svg>'''
with open('assets/scenes/project-autohr.svg', 'w', encoding='utf-8') as f:
    f.write(project_hr_content)

# 4. MISSION CONTROL: 736x414 (1.777778). Frame: 817.78 x 460.0 (1.7778)
ref9_inner = extract_inner_svg('assets/reference/Bookmarks _ X.svg', 'ref9')
mc_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 550" width="100%" height="100%">
  <defs>
    <linearGradient id="mcBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="60%" stop-color="#54152B" />
      <stop offset="100%" stop-color="#2D112C" />
    </linearGradient>

    <clipPath id="bookmarksClip">
      <rect x="40" y="40" width="817.78" height="460" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="550" fill="url(#mcBg)" />

  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="280" height="40" fill="#E86A33" rx="4" />
    <text x="140" y="26" font-family="'Courier New', monospace" font-size="15" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">MISSION CONTROL</text>
  </g>

  <rect x="36" y="96" width="825.78" height="418" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g transform="translate(40, 100)">
    <g clip-path="url(#bookmarksClip)" opacity="0.95">
      <g transform="translate(0, 0) scale(1.111111)">
        {ref9_inner}
      </g>
    </g>
  </g>

  <g transform="translate(900, 100)">
    <rect x="0" y="0" width="640" height="410" fill="#1A0A1F" stroke="#F5B041" stroke-width="2" rx="12" />
    
    <text x="40" y="55" font-family="'Impact', sans-serif" font-size="28" fill="#F5B041" letter-spacing="2">ACTIVE MISSIONS &amp; BUILDING LOGS</text>
    <text x="40" y="85" font-family="'Courier New', monospace" font-size="13" fill="#E86A33" font-weight="900">STATUS: TRANSMISSION ACTIVE // EARTH-2705</text>

    <g transform="translate(40, 130)" font-family="'Courier New', monospace" font-size="14" fill="#F5F1E8">
      <g transform="translate(0, 0)">
        <text x="0" y="0" font-weight="900" fill="#F5B041">→ AGENTIC AI ORCHESTRATION</text>
        <text x="25" y="25" fill="#D0C4DF">Building stateful execution graphs with memory.</text>
      </g>

      <g transform="translate(0, 75)">
        <text x="0" y="0" font-weight="900" fill="#E86A33">→ HIGH-PERFORMANCE RAG</text>
        <text x="25" y="25" fill="#D0C4DF">Optimizing dense search &amp; evidence retrieval.</text>
      </g>

      <g transform="translate(0, 150)">
        <text x="0" y="0" font-weight="900" fill="#F5F1E8">→ PRODUCTION AI INFRASTRUCTURE</text>
        <text x="25" y="25" fill="#D0C4DF">Deploying scalable FastAPI microservices &amp; PGVector.</text>
      </g>
    </g>
  </g>
</svg>'''
with open('assets/scenes/mission-control.svg', 'w', encoding='utf-8') as f:
    f.write(mc_content)

# 5. SCENE 08 / ENDING: 736x434 (1.6958525). Frame: 746.18 x 440.0 (1.6959)
ref10_inner = extract_inner_svg('assets/reference/download (3).svg', 'ref10')
scene08_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 580" width="100%" height="100%">
  <defs>
    <linearGradient id="nightEnding" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A0A1F" />
      <stop offset="40%" stop-color="#2D112C" />
      <stop offset="80%" stop-color="#54152B" />
      <stop offset="100%" stop-color="#09040D" />
    </linearGradient>

    <pattern id="endHalftone" x="0" y="0" width="12" height="12" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.5" fill="#E86A33" fill-opacity="0.15" />
    </pattern>

    <clipPath id="endArtClip">
      <rect x="40" y="40" width="746.18" height="440" rx="10" />
    </clipPath>
  </defs>

  <rect width="1600" height="580" fill="url(#nightEnding)" />
  <rect width="1600" height="580" fill="url(#endHalftone)" />

  <rect x="36" y="36" width="754.18" height="448" fill="#120D1A" stroke="#F5B041" stroke-width="2" rx="12" />
  <g clip-path="url(#endArtClip)" opacity="0.95">
    <g transform="translate(40, 40) scale(1.013831)">
      {ref10_inner}
    </g>
  </g>

  <g transform="translate(830, 80)">
    <rect x="0" y="0" width="730" height="360" fill="#1A0A1F" opacity="0.95" stroke="#F5B041" stroke-width="2" rx="12" />
    
    <text x="40" y="65" font-family="'Courier New', monospace" font-size="20" font-weight="900" fill="#F5B041">"Some systems answer questions."</text>
    <text x="40" y="115" font-family="'Impact', sans-serif" font-size="28" font-weight="900" fill="#F5F1E8" letter-spacing="2">"I WANT TO BUILD THE ONES THAT CHANGE WHAT HAPPENS NEXT."</text>

    <g transform="translate(40, 210)">
      <rect x="0" y="0" width="320" height="55" fill="#E86A33" rx="6" />
      <text x="160" y="36" font-family="'Impact', sans-serif" font-size="24" font-weight="900" fill="#F5F1E8" text-anchor="middle" letter-spacing="3">TO BE CONTINUED... 🕷️</text>
    </g>
  </g>
</svg>'''
with open('assets/scenes/scene08-ending.svg', 'w', encoding='utf-8') as f:
    f.write(scene08_content)

print("All frame dimensions refined to 100% exact mathematical ratio match.")
