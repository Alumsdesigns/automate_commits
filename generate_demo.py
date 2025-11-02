import os
from datetime import datetime

# List of demo techniques and inline CSS
DEMOS = [
    {
        "title": "Flexbox Demo",
        "technique": "CSS Flexbox",
        "css": """
        body { font-family: Arial, sans-serif; background: #f0f4ff; margin: 0; padding: 20px; }
        h1 { color: #2a4d9b; }
        p { color: #333; }
        .demo { display: flex; gap: 10px; margin-top: 20px; }
        .demo div { flex: 1; background: #c9d7ff; padding: 20px; text-align: center; border-radius: 8px; }
        """
    },
    {
        "title": "Grid Demo",
        "technique": "CSS Grid",
        "css": """
        body { font-family: Arial, sans-serif; background: #fff9f0; margin: 0; padding: 20px; }
        h1 { color: #c05a00; }
        p { color: #333; }
        .demo { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 20px; }
        .demo div { background: #ffd9b3; padding: 20px; text-align: center; border-radius: 8px; }
        """
    },
    {
        "title": "Fluid Typography",
        "technique": "Clamp & Fluid font-size",
        "css": """
        body { font-family: Arial, sans-serif; background: #f9f9ff; margin: 0; padding: 20px; }
        h1 { font-size: clamp(1.5rem, 4vw, 3rem); color: #4b0082; }
        p { font-size: clamp(1rem, 2vw, 1.5rem); color: #444; }
        .demo { margin-top: 20px; background: #e6e6ff; padding: 20px; border-radius: 8px; }
        """
    },
    {
        "title": "Clamp Sizing",
        "technique": "Responsive clamp() padding",
        "css": """
        body { font-family: Arial, sans-serif; background: #f0fff4; margin: 0; padding: 20px; }
        h1 { color: #006644; }
        p { color: #333; }
        .demo { background: #b3ffcc; padding: clamp(10px, 5vw, 50px); border-radius: 8px; }
        """
    }
]

SITE_DIR = "site"
os.makedirs(SITE_DIR, exist_ok=True)

# Count existing demos
existing = len([f for f in os.listdir(SITE_DIR) if f.endswith(".html")])

# Pick the next demo
demo = DEMOS[existing % len(DEMOS)]

# HTML template with embedded <style>
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{demo['title']}</title>
  <meta name="description" content="This page shows {demo['technique']} in action.">
  <style>
  {demo['css']}
  </style>
</head>
<body>
  <h1>{demo['title']}</h1>
  <p>This page shows {demo['technique']} in action.</p>
  <div class="demo">
    <div>Box 1</div>
    <div>Box 2</div>
    <div>Box 3</div>
    <p>Technique used: {demo['technique']}</p>
  </div>
</body>
</html>
"""

# Create unique filenames
timestamp = datetime.now().strftime("%Y%m%d%H%M")
html_file = os.path.join(SITE_DIR, f"{demo['title'].replace(' ', '').lower()}_{timestamp}.html")

# Write HTML file
with open(html_file, "w") as f:
    f.write(html_content)

print(f"✅ Generated demo: {html_file}")
