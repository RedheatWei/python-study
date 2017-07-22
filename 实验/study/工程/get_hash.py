import PIL
import Image
im = Image.open('image4.png')
box = (int(328), int(315),int(358),int(349))
region = im.crop(box)
#print im.format,im.size,im.mode
print region