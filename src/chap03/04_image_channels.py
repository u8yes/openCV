import cv2

image = cv2.imread('images/color.jpg', cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

if image.ndim != 3:
    raise Exception("컬러 영상 아님")
    # 컬러이기 때문에 3차원

bgr = cv2.split(image) # 채널 분리: 컬러 영상 - > 3채널 분리

print('bgr 자료형:', type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print('bgr 원소 개수:', len(bgr))

# 각 채널을 윈도우에 띄우기
cv2.imshow('image', image)
cv2.imshow('Blue channel', bgr[0])
cv2.imshow('green channel', bgr[1])
cv2.imshow('red channel', bgr[2])

cv2.waitKey(0)