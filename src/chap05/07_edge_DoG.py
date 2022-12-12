import numpy as np, cv2

image = cv2.imread("images/dog.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

gaus = cv2.GaussianBlur(image, (7, 7), 0) # 가우시안 마스크 적용
# default는 9 by 9가 일반적 # 표준편차는 0으로 가우시안 값을 적용
# Blur는 평균을 만들어서 이미지를 부드럽게 가져감.
dst1 = cv2.Laplacian(gaus, cv2.CV_16S, 7)

gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
dst2 = gaus1 - gaus2 # DoG 수행

cv2.imshow("image", image)
cv2.imshow("dst1 - LoG", dst1.astype("uint8"))
cv2.imshow("dst2 - DoG", dst2)
cv2.waitKey(0)





