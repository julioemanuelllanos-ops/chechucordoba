import json
import re

file_path = r'c:\Users\julio\.gemini\antigravity\scratch\chechu-cordoba\chechucordoba_landing_glitterbar.html at main · julioemanuelllanos-ops_chechucordoba.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for the JSON payload
match = re.search(r'<script type="application/json" data-target="react-app.embeddedData">(.*?)</script>', content)
if match:
    data = json.loads(match.group(1))
    raw_lines = data.get('payload', {}).get('codeViewBlobLayoutRoute.StyledBlob', {}).get('rawLines', [])
    if not raw_lines:
        # Try another path if the structure is different
        raw_lines = data.get('payload', {}).get('blob', {}).get('rawLines', [])
    
    if raw_lines:
        clean_content = '\n'.join(raw_lines)
        with open('landing_glitterbar_clean.html', 'w', encoding='utf-8') as out:
            out.write(clean_content)
        print("Extracted content to landing_glitterbar_clean.html")
    else:
        print("Could not find rawLines in the JSON payload.")
else:
    print("Could not find the JSON payload script tag.")
