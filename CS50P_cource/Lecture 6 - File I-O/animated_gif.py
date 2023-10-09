import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

#  python animated_gif.py robo_silver1.png robo_silver2.png robo_silver3.png robo_silver4.png
