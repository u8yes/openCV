import numpy as np, cv2

image = cv2.imread("06_images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
# 141 by 150
size = (350, 400)

dst1 = cv2.resize(image, size, interpolation=cv2.INTER_NEAREST) # 최근접 보간
dst2 = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR) # 양선형 보간
dst3 = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC) # 3차 회선 보간

cv2.imshow("image", image)
cv2.imshow("OpenCV-Nearest", dst1)
cv2.imshow("OpenCV-Bilinear", dst2)
cv2.imshow("OpenCV-Cubic", dst3)
cv2.waitKey(0)







