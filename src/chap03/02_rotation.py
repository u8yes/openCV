import cv2

image = cv2.imread("images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

x_axis = cv2.flip(image, 0) # x축
y_axis = cv2.flip(image, 1) # y축
xy_axis = cv2.flip(image, -1)
rep_image = cv2.repeat(image, 1, 2)
# ny, nx: 수직 방향, 수평 방향 반복 횟수
trans_image = cv2.tranpose(image)

# 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_image', 'trans_image']
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)