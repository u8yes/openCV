import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400,600,3), np.uint8)
# 컬러일 경우엔 channel이 추가되면서 3차원으로 진행됨.
# 3채널 컬러 영상 생성
image[:] = (255, 255, 255) # 흰색

pt1, pt2 = (50,50), (250,150) # 좌표 선언 - 정수형 튜플
pt3, pt4 = (400,150), (500,50)
roi = 50, 200, 200, 100

# 직선 그리기
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA) 
# 두께를 3으로 함. # LINE_AA 모양으로

# 사각형 그리기
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)
cv2.rectangle(image, (400,200,100,100), green, cv2.FILLED)

cv2.imshow('Line & Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows() # 모든 윈도우를 닫음.