import numpy as np, cv2

image = cv2.imread("images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 1) OpenCV 함수 이용
dst1 = cv2.add(image, 100)
# 영상 밝게(+) saturation 방식, 255가 넘어가면 다 255로 해줌.
dst2 = cv2.subtract(image, 100)
# 영상 어둡게(-), 0 밑이면 다 0으로

# 2) numpy array 이용
dst3 = image + 100   # 영상 밝게 modulo 방식
dst4 = image - 100   # 영상 어둡게

cv2.imshow("original image", image)
cv2.imshow("dst1 image", dst1)
cv2.imshow("dst2 image", dst2)
cv2.imshow("dst3 image", dst3)
cv2.imshow("dst4 image", dst4)
cv2.waitKey(0)
