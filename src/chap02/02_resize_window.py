import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 255

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.moveWindow(title1, 150, 150) # Position1위치 이동시키고 싶을 때 x:150, y:150
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0) # 0이하의 값을 넣어주면 키값이 입력될 때까지 대기함.
cv2.destroyAllWindows() # window창이 띄워져있으면 다 분쇄시킴.