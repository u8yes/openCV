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
data1 = [-1, 0, 1, # 프리윗 수직 마스크
         -1, 0, 1,
         -1, 0, 1]
# 수평 방향
data2 = [-1, -1, -1, # 프리윗 수평 마스크
         0, 0, 0,
         1, 1, 1]

dst, dst1, dst2 = differential(image, data1, data2) # 1차 미분 수행

cv2.imshow("image", image)
cv2.imshow("prewitt edge", dst)
cv2.imshow("dst1- vertical", dst1) # 좌측 대각선으로 적용
cv2.imshow("dst2- horizontal", dst2) # 우측 대각선으로 적용
cv2.waitKey(0)








