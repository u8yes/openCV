import numpy as np, cv2

image = cv2.imread("images/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

data1 = [[0, 1, 0],
         [1, -4, 1],
         [0, 1, 0]]

data2 = [[-1, -1, -1], # 전체를 합했을 때 0이 되게끔
         [-1,  8, -1], # 모든 방향성을 고려하게 됨
         [-1, -1, -1]] # 2차 미분

mask1 = np.array(data1, np.int16)
mask2 = np.array(data2, np.int16)

# OpenCV 함수 cv2.filter2D()를 통한 라플라시안 수행
dst1 = cv2.filter2D(image, cv2.CV_16S, mask1)
# CV_16S의 Sign은 -음수까지 넣어줌
dst2 = cv2.filter2D(image, cv2.CV_16S, mask2)
dst3 = cv2.Laplacian(image, cv2.CV_16S)

cv2.imshow("image", image)
cv2.imshow("filter2D 4-방향", cv2.convertScaleAbs(dst1))
cv2.imshow("filter2D 8-방향", cv2.convertScaleAbs(dst2))
cv2.imshow("Laplacian_OpenCV", cv2.convertScaleAbs(dst3))

cv2.waitKey(0)








