# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: drawshape.py
@time: 2023/5/27 17:28
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
#基本功能，通过按鼠标左键画基本图形
#画线，拖动鼠标，开始画线
#画矩形
#画圆形
#l=>0=>线； r=>1=>矩形； c=>2=>圆形
#设置回调函数

curshape = 0
startpos = (0, 0)
def mouse_callback(event, x, y, flags, userdata):
    #print(event, x, y, flags, userdata)
    global  startpos, curshape
    if (event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x,y)
    elif (event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if curshape == 0: #line
            cv2.line(img, startpos, (x,y), (0,0,255))
        elif curshape == 1:
            cv2.rectangle(img, startpos, (x, y), ( 0,255, 0))
        elif curshape == 2:
            a = x - startpos[0]
            b = y - startpos[1]
            r = int(math.sqrt(a**2 + b **2))
            cv2.circle(img, startpos, r, (255,255, 255))
        else:
            print("no shape")

#创建窗口
cv2.namedWindow("drawshape", cv2.WINDOW_NORMAL)
cv2.resizeWindow("drawshape", 640, 480)

#设置鼠标回调
cv2.setMouseCallback("drawshape", mouse_callback)

#显示窗口和背景
img = np.zeros((480, 640, 3), np.uint8)

while True:
    cv2.imshow("drawshape", img)
    key = cv2.waitKey(1) & 0xFF
    if key  ==ord("q"):
        break
    elif key == ord("l"):
        curshape = 0 #draw line
    elif key == ord("r"):
        curshape = 1
    elif key == ord("c"):
        curshape = 2
cv2.destroyAllWindows()