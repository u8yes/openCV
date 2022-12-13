import numpy as np, cv2

image = cv2.imread("06_images/affine.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
# image size 320x330

center = (200, 200) # 중심점
angle, scale = 30, 1
size = image.shape[::-1]

pt1 = np.array([(30, 70), (20, 240), (300, 110)], np.float32) # float32는 .0이 붙게 만듦.
pt2 = np.array([(120, 20), (10, 180), (280, 260)], np.float32) # 1차원

aff_mat = cv2.getAffineTransform(pt1, pt2)
rot_mat = cv2.getRotationMatrix2D(center, angle, scale) # affine 행렬 반환

dst1 = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)
dst2 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("dst1-affine", dst1)
cv2.imshow("dst2-affine_rotate", dst2)
cv2.waitKey(0)







