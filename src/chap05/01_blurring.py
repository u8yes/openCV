import numpy as np, cv2, time

def blur_convolution(image, filter):
    rows, cols = image.shape[:2] # 시작은 0부터 # 행과 열
    # height, width로 생각하는 게 더 쉽다.
    # 이미지는 300x270
    # rows = 270, cols = 300 # 270행, 300열
    dst = np.zeros((rows, cols), np.float32) # 270 by 300
    xcenter, ycenter = filter.shape[1]//2, filter.shape[0] // 2
    # filter는 3 by 3이다. 그래서 3/2 하면 몫 1이 나온다.
    # xcenter, ycenter는 둘 다 1이 됨.

    for i in range(ycenter, rows - ycenter): # 행만큼 반복하겠다.
        # ycenter를 만든 것은 다음으로 넘어가기 위함.
        # 270이 아닌 269에서 끝내야 하기 때문에 -1을 추가해준 것.
        # 1부터 시작하려고 center라고 한 것임.
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1 # 0, 3 저장 돼있음
            x1, x2 = j - xcenter, j + xcenter + 1 # 0, 3 저장 돼있음
            roi = image[y1:y2, x1:x2].astype("float32")
            # y1=0 ~ y2=3-1 까지, x도 동일하게.
            # 정수값을 실수값으로 바꿔줌.

            tmp = cv2.multiply(roi, filter)
            # 관심영역과 mask를 각각 곱해줌.
            dst[i, j] = cv2.sumElems(tmp)[0]
            # sumElems은 채널 별로 다 더해줌
            # 흑백이라서 첫번째 채널의 값만 읽어옴.
    return  dst

image = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 블러링 마스크 원소 지정
filter = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]
# filter를 총 1로 만들어줘야함.

mask = np.array(filter, np.float32).reshape(3, 3)
blur = blur_convolution(image, mask)

cv2.imshow("image", image)
cv2.imshow("blur", blur.astype("uint8"))
# 이미지는 정수값이어야 하기 때문에 실수값을 정수로 바꿔줌.

cv2.waitKey(0)
