import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE) # 알렉산더왕
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 영상 합성
alpha, beta = 0.6, 0.7 # 곱셈 비율
add_img1 = cv2.add(image1, image2)
add_img2 = cv2.add(image1*alpha, image2*beta)
add_img2 = np.clip(add_img2, 0, 255).astype("uint8")
# saturation 처리를 numpy 방식으로 처리 # 최소값 : 0 , 최대값 : 255으로 설정.
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)
# addWeighted는 가중치를 더함 # 자체적으로 합성을 수행하는 함수

titles = ['image1','image2','add_img1', 'add_img2', 'add_img3']
for t in titles:
    cv2.imshow(t, eval(t))

cv2.waitKey(0)

