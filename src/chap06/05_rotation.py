import numpy as np, cv2
from Common.interpolation import bilinear_value

def contain(p, shape): # 좌표(y,x)가 범위내 인지 검사
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x =  j * cos + i * sin

            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, [x, y])

    return dst

image = cv2.imread("06_images/rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
# 이미지 사이즈 360x360

dst1 = rotate(image, 30)
dst2 = rotate(image, 60)

cv2.imshow("image", image)
cv2.imshow("dst-30", dst1)
cv2.imshow("dst-60", dst2)

cv2.waitKey(0)

