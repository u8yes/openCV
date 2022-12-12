import numpy as np, cv2
from Common.filters import filter
# 함수를 직접 사용가능해짐.

image = cv2.imread("images/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 샤프닝 필터(마스크) 원소 지정
# 전체가 1이 되게끔 # 중심값을 크게 해줌.
data1 = [0, -1, 0,
         -1, 5, -1,
         0, -1, 0]

data2 = [[-1, -1, -1], # 다이렉트로 직접 처리가 가능하다.
         [-1, 9, -1],
         [-1, -1, -1]]

mask1 = np.array(data1, np.float32).reshape(3,3)
# filter에서는 실수로.
mask2 = np.array(data2, np.float32)
# reshape 필요없이 바로 2차원으로 만든다.

# 합성곱으로 filter해주는 함수를 사용.
sharpen1 = filter(image, mask1)
sharpen2 = filter(image, mask2)

sharpen1 = cv2.convertScaleAbs(sharpen1)
#scaleAbsulute - 음수로 나오는 것을 절대값을 씌움
sharpen2 = cv2.convertScaleAbs(sharpen2)

cv2.imshow("image", image)
cv2.imshow("sharpen1", sharpen1)
cv2.imshow("sharpen2", sharpen2)

cv2.waitKey(0)





