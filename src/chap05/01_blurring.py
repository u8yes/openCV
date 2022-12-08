import numpy as np, cv2, time

def blur_convolution(image, filter):
    rows, cols = image.shape[:2]
    np.zeros((rows, cols), np.float32)
    xcenter, ycenter = filter.shape[1]//2, filter.shape[0] // 2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            

image = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 블러링 마스크 원소 지정
filter = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]

mask = np.array(filter, np.float32).reshape(3, 3)



