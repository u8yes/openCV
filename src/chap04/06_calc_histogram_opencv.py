import numpy as np, cv2

def calc_histo(image, hsize, ranges=[0,256]): # 행렬 원소의 1차원 히스토그램 계산
    hist = np.zeros((hsize, 1), np.float32) # 히스토그램 누적 행렬
    gap = ranges[1] / hsize # 계급 간격

    for i in range(image.shape[0]): # 행의 갯수만큼 반복
        for j in range(image.shape[1]): # 열의 갯수만큼 반복
            idx = int(image.item(i, j) / gap)
            hist[idx] += 1

    return hist
    
image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

hsize, ranges = [32], [0, 256]
gap = ranges[1] / hsize[0]
ranges_gap = np.arange(0, ranges[1]+1, gap) # arange는 range와 동일한 기능이다.
hist1 = calc_histo(image, hsize[0], ranges)
hist2 = cv2.calcHist([image], [0], None, hsize, ranges) # 범주형
hist3, bins = np.histogram(image, ranges_gap) # 가장 수행시간 효율이 좋은 numpy

print("User 함수: \n", hist1.flatten())
print("OpenCV 함수: \n", hist2.flatten())
print("numpy 함수: \n", hist3) # numpy는 알아서 벡터의 형태로 만들어서 return해준다.

cv2.imshow("image", image)
cv2.waitKey(0)
