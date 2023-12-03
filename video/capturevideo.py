# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: capturevideo.py
@time: 2023/5/18 19:31
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
######################################
#读取视频文件
# cv.namedWindow("video", cv.WINDOW_NORMAL)
# cv.resizeWindow("video", 640, 480)
# #获取视频设备
# #cap = cv.VideoCapture(0)
# cap = cv.VideoCapture("sun.mp4")
# while cap.isOpened():
#     #从摄像头读取视频帧
#     ret, frame = cap.read()
#     if ret ==True:
#         cv.imshow("video", frame)
#         #等待键盘事件，如果为q，退出
#         key = cv.waitKey(20)
#         if (key & 0xFF == ord("q")):
#             break
#     else:
#         break
#     #释放capture
# cap.release()
# cv.destroyAllWindows()


# #读取视频文件并存为多媒体文件，
# cap = cv.VideoCapture(0)
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# print("width:",width, "height:", height)
# fourcc = cv.VideoWriter_fourcc(*"mp4v")
# vw = cv.VideoWriter("out.mp4", fourcc, 25, (width, height))
# #创建窗口
# cv.namedWindow("video", cv.WINDOW_NORMAL)
# cv.resizeWindow("video", 640, 480)
# # #获取视频设备
#
# while cap.isOpened():
#     #从摄像头读取视频帧
#     ret, frame = cap.read()
#     if ret == True:
#         #将视频帧在窗口展示
#         vw.write(frame)
#         cv.imshow("video", frame)
#         #cv.resizeWindow("video", 640, 360)
#         #写数据到多媒体文件
#
#         #等待键盘事件，如果为q,退出
#         key = cv.waitKey(1)
#         if(key &0xFF == ord("q")):
#             break
#     else:
#         break
# #释放VideoCapture
# cap.release()
# #释放VideoWriter
# vw.release()
# cv.destroyAllWindows()

#合并视频文件

import cv2

# 读取第一个视频文件
input_video1 = cv2.VideoCapture('video1.mp4')  # 替换为第一个视频文件路径
fps1 = input_video1.get(cv2.CAP_PROP_FPS)
width1 = int(input_video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(input_video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 读取第二个视频文件
input_video2 = cv2.VideoCapture('video2.mp4')  # 替换为第二个视频文件路径
fps2 = input_video2.get(cv2.CAP_PROP_FPS)
width2 = int(input_video2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(input_video2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 读取第二个视频文件
input_video3 = cv2.VideoCapture('video3.mp4')  # 替换为第二个视频文件路径
fps3 = input_video2.get(cv2.CAP_PROP_FPS)
width3 = int(input_video2.get(cv2.CAP_PROP_FRAME_WIDTH))
height3 = int(input_video2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 读取第二个视频文件
input_video4 = cv2.VideoCapture('video4.mp4')  # 替换为第二个视频文件路径
fps4 = input_video2.get(cv2.CAP_PROP_FPS)
width4 = int(input_video2.get(cv2.CAP_PROP_FRAME_WIDTH))
height4 = int(input_video2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置输出视频文件的参数为第一个视频文件的参数
output_video = cv2.VideoWriter('merged_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps1, (width1, height1))

# 读取并写入第一个视频文件的帧
while True:
    ret1, frame1 = input_video1.read()
    if not ret1:
        break
    output_video.write(frame1)

# 读取并写入第二个视频文件的帧
while True:
    ret2, frame2 = input_video2.read()
    if not ret2:
        break
    output_video.write(frame2)

# 读取并写入第二个视频文件的帧
while True:
    ret3, frame3 = input_video3.read()
    if not ret3:
        break
    output_video.write(frame3)

# 读取并写入第二个视频文件的帧
while True:
    ret4, frame4 = input_video4.read()
    if not ret4:
        break
    output_video.write(frame4)

# 释放资源
input_video1.release()
input_video2.release()
input_video3.release()
input_video4.release()
output_video.release()
cv2.destroyAllWindows()



