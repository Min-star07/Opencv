# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: scale.py.py
@time: 2023/5/31 14:06
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("xiaoxiannv2.jpg")
print(img.shape)
#缩放
#img_resize = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
img_resize = cv2.resize(img, dsize=None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
#翻转  0 上下 ； >0 左右 <0，上下+左右
img_filp_0 = cv2.flip(img_resize, 0)
img_filp_1 = cv2.flip(img_resize, 1)
img_filp_11 = cv2.flip(img_resize, -1)
#图像旋转
img_rotate = cv2.rotate(img_resize, cv2.ROTATE_180)
#仿射变换是图像旋转，缩放，平移的总称
# cv2.imshow("img", img)
# cv2.imshow("img_resize", img_resize)
# cv2.imshow("img_filp_0", img_filp_0)
# cv2.imshow("img_filp_1", img_filp_1)
# cv2.imshow("img_filp_11", img_filp_11)
# cv2.imshow("img_ratate", img_rotate)
# cv2.waitKey(0)
# 创建Matplotlib画布
fig, axes = plt.subplots(2, 3, figsize=(10, 10))

# 在画布上显示四则运算后的图像
axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title('img')
axes[0, 0].axis('off')

axes[0, 1].imshow(cv2.cvtColor(img_filp_0, cv2.COLOR_BGR2RGB))
axes[0, 1].set_title('img_filp_0')
axes[0, 1].axis('off')


axes[0, 2].imshow(cv2.cvtColor(img_rotate, cv2.COLOR_BGR2RGB))
axes[0, 2].set_title('img_rotate')
axes[0, 2].axis('off')

axes[1, 0].imshow(cv2.cvtColor(img_filp_1, cv2.COLOR_BGR2RGB))
axes[1, 0].set_title('img_filp_1')
axes[1, 0].axis('off')

axes[1, 1].imshow(cv2.cvtColor(img_filp_11, cv2.COLOR_BGR2RGB))
axes[1, 1].set_title('img_filp_11')
axes[1, 1].axis('off')

axes[1, 2].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[1, 2].set_title('img')
axes[1, 2].axis('off')


# 调整子图之间的间距
plt.tight_layout()

# 显示图片
plt.show()
