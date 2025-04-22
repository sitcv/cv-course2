import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("lena.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) ##注意： opencvが画像を読んだら、カラー成分はBGRになります。
img_blurred = cv2.GaussianBlur(img_rgb, (11,11), 10)
dst = cv2.addWeighted(img_rgb, 2, img_blurred, -1.0, 0) # im1 = im + (im - im_blurred) = 2* im - im_blurred
plt.imshow(dst)
plt.show()