# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: sobel.py
@time: 2023/6/1 14:54
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  cv2
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img", 540, 720)
img = cv2.imread("xiaoxainnv.jpg")
#索贝尔算子，同时求x，y效果不好
# d1 = cv2.Sobel(img, cv2.CV_64F,1, 0, ksize=5)
# d2 = cv2.Sobel(img, cv2.CV_64F,0, 1, ksize=5)
# dst =d1+d2
#dst = cv2.add(d1,d2)
#Scharr算子
# d1 = cv2.Scharr(img, cv2.CV_64F,1, 0)
# d2 = cv2.Scharr(img, cv2.CV_64F,0, 1)
# dst =d1+d2
#dst = cv2.add(d1,d2)
#拉普拉斯算子，可以同时计算两个，但是噪声比较明显，一般先去噪
#dst = cv2.Laplacian(img, cv2.CV_64F,ksize=5)
# cv2.imshow("d1", d1)
# cv2.imshow("d2", d2)

#边缘检测
#img= cv2.imread("luna.png")
dst = cv2.Canny(img, 100, 110)
cv2.imshow("img", dst)

cv2.waitKey(0)