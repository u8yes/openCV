import numpy as np, cv2, time

def blur_convolution(image, filter):
    rows, cols = image.shape[:2]
    # height, width로 생각하는 게 더 쉽다.
    # 300, 270
    dst = np.zeros((rows, cols), np.float32)
    xcenter, ycenter = filter.shape[1]//2, filter.shape[0] // 2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1 # 1, 3 저장 돼있음
            x1, x2 = j - xcenter, j + xcenter + 1 # 1, 3 저장 돼있음
            roi = image[y1:y2, x1:x2].astype("float32")

            tmp = cv2.multiply(roi, filter)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return  dst

image = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 블러링 마스크 원소 지정
filter = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]

mask = np.array(filter, np.float32).reshape(3, 3)
blur = blur_convolution(image, mask)

cv2.imshow("image", image)
cv2.imshow("blur", blur.astype("uint8"))

cv2.waitKey(0)