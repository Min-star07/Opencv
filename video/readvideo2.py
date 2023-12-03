# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: readvideo2.py
@time: 2023/12/3 20:00
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 加载人脸检测器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 读取视频
video_capture = cv2.VideoCapture('video2.mp4')  # 替换为你的视频文件路径

while True:
    # 读取一帧视频
    ret, frame = video_capture.read()

    if not ret:
        break

    # 将图像转换为灰度图像（人脸检测器需要灰度图像）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 在检测到的人脸周围画框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('Video', frame)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
video_capture.release()
cv2.destroyAllWindows()
