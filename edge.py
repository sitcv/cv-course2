#canny edge detectionを使って、girlの画像をエッジ検出する
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 画像を読み込む
img = cv2.imread('girl.jpg')

# グレースケールに変換する
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ガウシアンフィルタでノイズを除去する
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

# Cannyエッジ検出を適用する
edges = cv2.Canny(img_blur, 100, 200)

# 結果を表示する
plt.imshow(edges, cmap='gray')
plt.show()
