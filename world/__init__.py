#make a world-generator, bitmap based.

from pgmagick import Image, DrawableCircle, DrawableText, Geometry, Color

im = Image(Geometry(300, 300), Color("yellow"))

circle = DrawableCircle(100, 100, 20, 20)
im.draw(circle)

im.fontPointsize(65)
text = DrawableText(30, 250, "Hello pgmagick")
im.draw(text)

im.write('test.png')