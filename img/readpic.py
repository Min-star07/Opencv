# -*- coding: utf-8 -*-

"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: readpic.py
@time: 2023/12/3 18:22
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
cv.namedWindow("img", cv.WINDOW_NORMAL)
cv.resizeWindow("img", 540, 720)
img = cv.imread("xiaoxainnv.jpg")
print(img.shape)
while True:
    cv.imshow("img", img)
    key = cv.waitKey(0) #unit ms
    # print(ord("q"))
    # print(key)
    if (key & 0xFF ==ord("q")):
        break
    elif (key & 0xFF ==ord("s")):
        cv.imwrite("xiaoxainnv1.jpg", img)
    cv.destroyAllWindows()

