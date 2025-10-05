from numpy import random as r
import cv2

#グレイ画像を読で、ランダムノイズを追加して、画像'girl_noise.png'として保存して。
img = cv2.imread('girl.jpg')

# 画像のサイズを取得
h, w = img.shape[:2]

# ノイズ生成
noise = r.rand(h,w)

# ノイズを画像に追加
img_noise = img.copy()
img_noise[noise < 0.1] = 0      # 1%の画素を黒に
img_noise[noise > 0.9] = 255    # 1%の画素を白に

cv2.imwrite('girl_noise.png', img_noise)    
cv2.imshow('img_noise', img_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()





