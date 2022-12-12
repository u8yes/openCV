import numpy as np, cv2
from Common.filters import filter

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1) # x분의 증가량
    dst2 = filter(image, mask2) # y분의 증가량

    dst = cv2.magnitude(dst1, dst2) # 제곱해서 루트씌우는 식

    # edge 검출에 대한 시각화
    dst = cv2.convertScaleAbs(dst)
    dst1 = cv2.convertScaleAbs(dst1)
    dst2 = cv2.convertScaleAbs(dst2)

    return dst, dst1, dst2

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

# 수직 방향
data1 = [-1, 0, 1, # 프리윗 수평 마스크
         -2, 0, 2,
         -1, 0, 1]
# 수평 방향
data2 = [-1, -2, -1, # 프리윗 수직 마스크
         0, 0, 0,
         1, 2, 1]

dst, dst1, dst2 = differential(image, data1, data2) # 1차 미분 수행

#OpenCV 제공 소벨 엣지 계산
dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0) # x를 편미분
dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1) # y를 편미분
dst3 = cv2.convertScaleAbs(dst3) # 0~255, 정수형으로 모두 변환
dst4 = cv2.convertScaleAbs(dst4)

cv2.imshow("image", image)

cv2.imshow("sobel edge", dst)
cv2.imshow("dst1- vertical", dst1)
cv2.imshow("dst2- horizontal", dst2)
cv2.imshow("dst3- vertical_OpenCV", dst3)
cv2.imshow("dst4- horizontal_OpenCV", dst4)
cv2.waitKey(0)


