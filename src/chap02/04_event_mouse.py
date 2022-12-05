import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("마우스 오른쪽 버튼 더블클릭")

image = np.full((200,300), 255, np.uint8) # unsigned integer 8

title1, title2 = "Mouse Event1", "Mouse Event2"
cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.setMouseCallback('Mouse Event1', onMouse)
# 호출할 목적 함수가 아니라 cv라이브러리에서
# 이미 등록해서 callback함수를 통해서 운영체제가 먼저 감지함
# '마우스 콜백 함수'

cv2.waitKey()
cv2.destroyAllWindow()