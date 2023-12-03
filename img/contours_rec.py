# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: contours.py
@time: 2023/6/1 18:47
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
def drawshape(src, points):
    i = 0
    while i < len(points):
        if i == len(points)-1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        else:
            x,y = points[i][0]
            x1, y1 = points[i+1][0]
            cv2.line(src,(x,y), (x1,y1), (0,0,255), 1)
        i = i+1

img = cv2.imread("../test3.jpg")
print(img.shape)
#img = cv2.resize(img, dsize=None, fx=3, fy =3)
#转变成单通道
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)
cv2.imshow("img", img_gray)
#二值化
ret, binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
#轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(contours)
#绘制轮廓
# i = 0
# print(len(contours))
# while i < len(contours):
#     cv2.drawContours(img, contours, i, (0,0,255), 3)
#     i = i +1
#     cv2.imshow("img_contour_%d"%(i), img)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

#计算面积和周长
#计算面积
# area = cv2.contourArea(contours[0])
# print("area : contours[0] = %d"%(area))
# #计算周长
# len = cv2.arcLength(contours[0], True)
# print("s : contours[0] = %d"%(len))

#计算最小外接矩阵
r = cv2.minAreaRect(contours[0])
print(r)
box = cv2.boxPoints(r)
print(box)
box = np.int0(box)
print(box)
cv2.drawContours(img, [box], 0, (0,255,0), 2)

x,y, w, h= cv2.boundingRect(contours[0])
cv2.rectangle(img, (x,y), (x+w, y +h),(255, 0,0), 2)
cv2.imshow("img_contour", img)
cv2.waitKey(0)