import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("images/equalize.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

# 영상의 히스토그램 계산
bins, ranges = [256], [0, 256]
hist = cv2.calcHist([image], [0], None, bins, ranges)

# 히스토그램 누적합 계산
accum_hist = np.zeros(hist.shape[:2], np.float32) # histogram의 행과 열
accum_hist[0] = hist[0]
for i in range(1, hist.shape[0]):
    accum_hist[i] = accum_hist[i - 1] + hist[i]

# 누적합의 정규화
accum_hist = (accum_hist / sum(hist)) * 255
dst1 = [[accum_hist[val] for val in row] for row in image]
dst1 = np.array(dst1, np.uint8)

dst2 = cv2.equalizeHist(image) # histogram으로 평활화시킴

hist1 = cv2.calcHist([dst1], [0], None, bins, ranges) # 내가 계산한 것
hist2 = cv2.calcHist([dst2], [0], None, bins, ranges) # cv2 평활하 기능을 사용해본 것

hist_img = draw_histo(hist) # 원 이미지에 대한 시각화
hist1_img = draw_histo(hist1)
hist2_img = draw_histo(hist2)

cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)

cv2.imshow("dst1_directly", dst1)
cv2.imshow("hist1_directly", hist1_img)

cv2.imshow("dst2_cv", dst2)
cv2.imshow("hist2_cv", hist2_img)

cv2.waitKey(0)
