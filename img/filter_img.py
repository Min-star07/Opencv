# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: filter_img.py
@time: 2023/6/1 14:30
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("niannian.jpg")
img = cv2.resize(img, dsize=None, fx=0.3, fy=0.3)
#滤波1
# kernel = np.ones((5,5), np.float32) / 32
# dst= cv2.filter2D(img, -1, kernel)
#方框滤波
#dst = cv2.blur(img, (5,5))
#高斯滤波
# dst  = cv2.GaussianBlur(img,(5,5), sigmaX=1)
#中值滤波
#dst = cv2.medianBlur(img, 5)
#双边滤波
dst = cv2.bilateralFilter(img, 7, 20, 50)
cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)