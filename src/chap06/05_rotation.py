import numpy as np, cv2

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)

image = cv2.imread("06_images/rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
# 이미지 사이즈 360x360













