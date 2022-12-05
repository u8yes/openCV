import numpy as np
import cv2

image = np.zeros((300, 400), np.uint8) # int8비트
image.fill(200)

cv2.imshow("window title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()