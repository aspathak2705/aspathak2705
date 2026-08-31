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
    
    # Extract inner elements
    svg_match = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
    if svg_match:
        return svg_match.group(1).strip()
    return content.strip()

print("Extraction script ready.")
