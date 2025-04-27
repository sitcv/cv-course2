from numpy import random as r
from matplotlib import pyplot as p
im = r.rand(256,256)
p.imshow(im, cmap='gray')
p.show()

