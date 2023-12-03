# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: draw.py
@time: 2023/5/27 16:24
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = np.zeros((480, 640,3), np.uint8)
#画线
cv2.line(img, (500, 20), (500, 400), (0,0,255), 5, 16) #线性-1,4, 8,16
#画矩形
cv2.rectangle(img, (10,10), (100, 100), (0,255,0), -1)

#画圆形
cv2.circle(img, (300, 300), 20, (255, 0, 0),1,16)
cv2.circle(img, (300, 300), 100, (255, 0, 0), 1, 8)
#画椭圆
#angle 是在左边开始顺时针转
#startangle是在右边开始顺时针转
cv2.ellipse(img, (300, 300), (100, 50), 0, 0, 360, (0,0, 255))

#画多边形
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
cv2.polylines(img, [pts], True, (0,0,255))
#填充
cv2.fillPoly(img, [pts], (0,255,0))

##填充文本
cv2.putText(img, "Hello World", (20, 400), cv2.FONT_HERSHEY_PLAIN ,1, (0,0,255))
cv2.imshow("draw", img)
cv2.waitKey(0)

