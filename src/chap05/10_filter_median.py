import numpy as np, cv2

def median_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2

    for i in range(center, rows - center):
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            mask = image[y1:y2, x1:x2].flatten()

            sort_mask = cv2.sort(mask, cv2.SORT_EVERY_COLUMN)
            dst[i, j] = sort_mask[sort_mask.size//2]
    return dst

image = cv2.imread("images/median.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
    
med_img1 = median_filter(image, 3)                            # 사용자 정의 함수
med_img2 = cv2.medianBlur(image, 3)                          # OpenCV 제공 함수


cv2.imshow("image", image),
cv2.imshow("median - User", med_img1)
cv2.imshow("median - OpenCV", med_img2)
cv2.waitKey(0)