# -*- coding: utf-8 -*-
"""
7주차. OpenCV 기반 영상처리 1

@author: cspark@iscu.ac.kr
"""

import cv2
import numpy as np

imgfile = 'wall-e-in-trashworld.jpg'
img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

cv2.namedWindow('Wall-E',cv2.WINDOW_NORMAL)

img_crop = img[1:100, 1:100]
img[301:400, 101:200] = img_crop

cv2.imshow('Wall-E',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

