import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400,600,3), np.uint8)
# 컬러일 경우엔 channel이 추가되면서 3차원으로 진행됨.
# 3채널 컬러 영상 생성
image[:] = (255, 255, 255) # 흰색

pt1, pt2 = (50,50), (250,150) # 좌표 선언 - 정수형 튜플
