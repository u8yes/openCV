import numpy as np, cv2
from Common.filters import filter

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1) # x분의 증가량
    dst2 = filter(image, mask2) # y분의 증가량

    dst = cv2.magnitude(dst1, dst2) # 제곱해서 루트씌우는 식
    dst1, dst2 = np.abs(dst1), np.abs(dst2) # 음수값이 반영되도록

    # edge 검출에 대한 시각화
    dst = np.clip(dst, 0, 255).astype("uint8")
    # 최대 255가 넘어가는 값은 255로, 0 이하는 0으로
    dst1 = np.clip(dst1, 0, 255).astype("uint8")
    dst2 = np.clip(dst2, 0, 255).astype("uint8")

    return dst, dst1, dst2


image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

data1 = [-1, 0, 0,
         0, 1, 0,
         0, 0, 0]

data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]

dst, dst1, dst2 = differential(image, data1, data2) # 1차 미분 수행

cv2.imshow("image", image)
cv2.imshow("roberts edge", dst)
cv2.imshow("dst1", dst1) # 좌측 대각선으로 적용
cv2.imshow("dst2", dst2) # 우측 대각선으로 적용
cv2.waitKey(0)








