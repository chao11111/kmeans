import sys
import os.path
import numpy as np
from kmeans import Kmeans
from PIL import Image

args = sys.argv
a = args[1]
b = args[2]
name, ext = os.path.splitext(a)
out = "{0}_reduced_{1}.bmp".format(name, b)

x = Image.open(a)
rgb = np.array(x.convert('RGB').getdata())

kmeans = Kmeans(int(b))
x.putdata(kmeans.compress(rgb))
x.save(out)
