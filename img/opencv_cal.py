# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: opencv_cal.py
@time: 2023/5/28 10:11
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
#
# cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("img", 540, 720)
img1 = cv2.imread("xiaoxainnv.jpg")
img2 = cv2.imread('xiaoxiannv2.jpg')
# 将图片大小调整为相同
# img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
img2 = np.ones((1440,1080, 3), np.uint8) * 10
print(img1.shape)
print(img2.shape)
# cv2.imshow("img", img)
cv2.putText(img1, "NIANGG ZI", (20, 400), cv2.FONT_HERSHEY_PLAIN ,10, (0,0,255))

#加法
addition = cv2.add(img1, img2)
# cv2.imshow("img_add", img_add)
#减法
subtraction = cv2.subtract(img1, img2)
# cv2.imshow("img_sub", img_sub)
#乘法
multiplication = cv2.multiply(img1, img2)
# cv2.imshow("img_multiply", img_multiply)
#除法
division= cv2.divide(img1, img2)
# cv2.imshow("img_divide", img_divide)

# 创建Matplotlib画布
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# 在画布上显示四则运算后的图像
axes[0, 0].imshow(cv2.cvtColor(addition, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title('Addition')
axes[0, 0].axis('off')

axes[0, 1].imshow(cv2.cvtColor(subtraction, cv2.COLOR_BGR2RGB))
axes[0, 1].set_title('Subtraction')
axes[0, 1].axis('off')

axes[1, 0].imshow(cv2.cvtColor(multiplication, cv2.COLOR_BGR2RGB))
axes[1, 0].set_title('Multiplication')
axes[1, 0].axis('off')

axes[1, 1].imshow(cv2.cvtColor(division, cv2.COLOR_BGR2RGB))
axes[1, 1].set_title('Division')
axes[1, 1].axis('off')

# 调整子图之间的间距
plt.tight_layout()

# 显示图片
plt.show()
# cv2.waitKey(0)
