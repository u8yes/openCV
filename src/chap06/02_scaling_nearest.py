import numpy as np, cv2

def scaling(img, size): # 크기 변경 함수
    # size - 축소, 확대하고자 하는 인폼 전달 받기
    dst = np.zeros(size[::-1], img.dtype)
    # size값이 역순으로 해당 크기를 만들어줌.
    # img와 동일하게 dataType을 잡아줌.
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    # 행ratioY,열ratioX을 나누어주면 비율이 나누어진다.
    # 원본이랑 나누기 해서 비율을 계산, 그러면 1이 나오게 됨.
    y = np.arange(0, img.shape[0], 1) # 0 ~ 299까지 step 1씩 증가시킴.
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x) # 직사각형의 격자가 만들어져서 반환됨
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]
    return dst