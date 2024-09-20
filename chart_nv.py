from PIL import Image
import sys

fname = sys.argv[1]
show = sys.argv[2] if len(sys.argv) > 2 else "false" 
img = Image.open(fname)
img = img.convert("RGBA")
pixdata = img.load()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y] == (255, 255, 255, 255): # if white then turn pixel to black
            pixdata[x, y] = (0, 0, 0, 255) 
        else:
            pd = pixdata[x, y]
            pixdata[x, y] = (255 - pd[0], 0, 0, 255) # if not white use the 255 - R channel value of pixel 
 
if show == "show":
    img.show()          

img.save(fname.replace(".png", "_NV.png"))
img.close()