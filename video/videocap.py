# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: videocap.py
@time: 2023/7/29 11:51
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import cv2
cv2.namedWindow("IP CAMERA", cv2.WINDOW_NORMAL)
cv2.resizeWindow("IP CAMERA", 640, 480)
print("Before URL")
cap = cv2.VideoCapture('rtsp://admin:Min08240707@192.168.3.86/11')
print("After URL")
if not cap.isOpened():
    print("无法打开摄像头")
    exit()
while cap.isOpened():
    #从摄像头读取视频帧
    ret, frame = cap.read()
    if ret ==True:
        cv2.imshow("IP CAMERA", frame)
        #等待键盘事件，如果为q，退出
        key = cv2.waitKey(20)
        if (key & 0xFF == ord("q")):
            break
    else:
        break
    #释放capture
cap.release()
cv2.destroyAllWindows()