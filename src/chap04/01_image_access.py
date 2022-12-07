import numpy as np, cv2, time

def pixel_access1(image): # 1) 파이썬을 이용해 접근한 방법
    image1 = np.zeros(image.shape[:2], image.dtype) # 행과 열의 값이라서 [:2]
    for i in range(image.shape[0]): # 행의 갯수만큼 반복
        for j in range(image.shape[1]): # 열의 갯수만큼 반복
            pixel = image[i, j]
            image1[i, j] = 255 - pixel # 리스트 형태로 다 반전해줌.
    return image1

def pixel_access2(image): # 2) openCV를 이용한 방법
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j) # cv2가 제공해주는 기능
            image2.itemset((i,j),255 - pixel)
    return image2

def pixel_access3(image):
    lut = [255 - i for i in range(256)] # lookup 테이블 생성 - LookUpTable
    lut = np.array(lut,np.uint8)
    image3 = lut[image]
    return image3

def pixel_access4(image): # 가장 간단하게 구현
    image4 = cv2.subtract(255, image)
    return image4

def pixel_access5(image):
    image5 = 255 - image
    return image5


image = cv2.imread("images/bright.jpg", cv2.IMREAD_GRAYSCALE) # 2차원 회색
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 수행 시간 체크
def time_check(func, msg):
    start_time = time.perf_counter() # performance 현재 시간 가져오기
    ret_img = func(image)
    elaped = (time.perf_counter() - start_time) * 1000 
    # 그동안의 시간 비교해보기 # 밀리세컨드 단위 # *1000을 하면 1초로
    print(msg, "수행시간 : %.2f ms" % elaped) # msg - 전달받은 메세지 출력
    return ret_img

image1 = time_check(pixel_access1, "[방법1] 직접 접근 방식")
image2 = time_check(pixel_access2, "[방법2] item() 함수 방식")
image3 = time_check(pixel_access3, "[방법3] 룩업테이블 접근 방식")
image4 = time_check(pixel_access4, "[방법4] OpenCV 방식")
image5 = time_check(pixel_access5, "[방법5] ndarray 연산 방식")

# 결과 영상 보기
cv2.imshow("image - original", image)
cv2.imshow("image1 - directly access", image1)
cv2.imshow("image2 - item()/itemset", image2)
cv2.imshow("image3 - LUT", image3)
cv2.imshow("image4 - OpenCV", image4)
cv2.imshow("image5 - ndarray", image5)
cv2.waitKey(0)



