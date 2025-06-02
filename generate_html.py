import os

wallpaper_folder = "wallpapers"
output_file = "index.html"

images = [f for f in os.listdir(wallpaper_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Wallpaper Gallery</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
  <h1>🖼️ Auto Wallpaper Gallery</h1>
  <div class="gallery">
'''

for img in images:
    html += f'''
    <div class="card">
      <img src="{wallpaper_folder}/{img}" alt="{img}">
      <a href="{wallpaper_folder}/{img}" download class="btn">Download</a>
    </div>
    '''

html += '''
  </div>
</div>
</body>
</html>
'''

with open(output_file, 'w') as f:
    f.write(html)

print(f"✅ index.html updated with {len(images)} wallpapers.")

