# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: car.py
@time: 2023/6/2 9:30
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def center(x,y, w, h):
    x1 = int(w/2.0)
    y1 = int(h/2.0)
    cx = x + x1
    cy= y + y1
    return cx, cy

min_w = 90
min_h = 90
cars = []
#检测线的高度
line_high = 600
#线的偏移
offset = 6
#车的统计
carno = 0
cap = cv2.VideoCapture("video2.mp4")
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()
#test = cv2.bgsegm.createBackgroundSubtractorMOG()
#形态学kernel
kernel =cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
while True:
    ret, frame = cap.read()
    if (ret == True):
        #灰度化
        # print(frame.shape)
        # exit()
        cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        #高斯去噪
        blur = cv2.GaussianBlur(frame,(3,3), 5)
        #去背景
        mask = bgsubmog.apply(blur)
        #t1 = test.apply(frame)
        #形态学操作
        #腐蚀操作,去掉小的斑块
        erode = cv2.erode(mask, kernel)
        #膨胀操作,还原放大
        dilate = cv2.dilate(erode, kernel, iterations=3)
        #闭操作，去掉物体内部的小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        #close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        cnts, h = cv2.findContours(close, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # cv2.line(frame, (10, line_high), (1200, line_high), (0,255,0), 2)
        for i, c in enumerate(cnts):
            x,y,w,h = cv2.boundingRect(c)

            #对车辆的宽高进行检测，已验证是否有效车辆
            isvalid = (w>min_w) and (h > min_h)
            if not isvalid:
                continue

            #到这里都是有效车辆
            cpoint= center(x, y, w, h)
            cars.append(cpoint)
            #判断中心点在线的附近
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # for x, y in cars:
            #     #要有一条线
            #    #范围 6
            #     if y > line_high - offset and y < line_high + offset:
            #         carno += 1
            #         cars.remove((x,y))
            #         print(carno)
        # cv2.putText(frame, "car count: " + str(carno), (600, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
        #cv2.imshow("video", mask)
        #cv2.imshow("erode", erode)
        # cv2.imshow("dilate", dilate)
        # cv2.imshow("close", close)
        cv2.imshow("result", frame)
        #cv2.imshow("video2", t1)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

