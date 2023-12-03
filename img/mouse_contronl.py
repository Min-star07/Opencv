# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: mouse_contronl.py
@time: 2023/5/25 9:05
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
#设置回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)
#设置窗口
cv.namedWindow("mouse", cv.WINDOW_NORMAL)
cv.resizeWindow("mouse", 640, 480)
#设置鼠标回调
cv.setMouseCallback("mouse", mouse_callback, "666")
#设置窗口和背景
img = np.zeros((480, 640, 3), np.uint8)
while True:
    cv.imshow("mouse", img)
    key = cv.waitKey(1)
    if key & 0xFF == ord("q"):
        break
cv.destroyAllWindows()
