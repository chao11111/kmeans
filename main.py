# -*- coding: utf-8 -*-
import sys
from kmeans import *
from PIL import Image
import os.path

args = sys.argv
a = args[1]
b = args[2]
name, ext = os.path.splitext(a)
out = "{0}_reduced_{1}.bmp".format(name, b)

x = Image.open(a)
rgb = list(x.convert('RGB').getdata())
x.putdata(kmeans(rgb, int(b)))
x.save(out)
