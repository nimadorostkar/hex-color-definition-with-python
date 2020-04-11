from PIL import Image
import webcolors
from colorthief import ColorThief

image_path = '1.jpg'

with open(image_path, 'r+b') as f:
    with Image.open(f) as image:


        # Get Colors
        color_thief = ColorThief(image_path)
        color_palette = color_thief.get_palette(color_count=4, quality=10)
        for color in color_palette:
            print(webcolors.rgb_to_hex(color))
