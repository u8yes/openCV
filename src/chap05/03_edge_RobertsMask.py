import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image in None: raise Exception("영상 파일 읽기 오류")

data1 = [-1, 0, 0,
         0, 1, 0,
         0, 0, 0]

data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]









