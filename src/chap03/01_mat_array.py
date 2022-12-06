import cv2
import numpy as np
import matplotlib.pyplot as plt

# 흑백 이미지로 로드
image = cv2.imread("./images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)
# IMREAD_GRAYSCALE 회색으로 바로 바꿔줌.

# 64 X 64 크기로 변경
image_64_64 = cv2.resize(image, (64, 64))

plt.imshow(image_64_64, cmap="gray") # cmap 컬러출력
plt.axis("off")
plt.savefig(fname="image_64_64.png", dpi=300)
plt.show()