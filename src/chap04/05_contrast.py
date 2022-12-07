import numpy as np, cv2

image = cv2.imread("images/contrast.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

noimage = np.zeros(image.shape[:2], image.dtype)
# image와 동일한 data type으로 설정 # 더미 영상으로 만들어줌
# noimage에는 0만 담아져있음.

avg = cv2.mean(image)[0] / 2.0 # 평균을 구한 후에 2를 나눔, 그래서 반이 됨.

dst1 = cv2.scaleAdd(image, 0.2, noimage) + 20 # 영상 대비 감소
# 20을 더해줘서 아예 어두워짐 방지해줌.
dst2 = cv2.scaleAdd(image, 2.0, noimage) # 영상대비 증가
dst3 = cv2.addWeighted(image, 0.5, noimage, 0, avg) 
# 전체 더 낮게 # 명암 대비 반 감소
# 부드러운 형태로 보여줌.
dst4 = cv2.addWeighted(image, 2.0, noimage, 0, -avg) 
# 전체 2배로 # 명암 대비 증가

# 영상 띄우기
cv2.imshow("image", image)
cv2.imshow("dst1 - decreate contrast", dst1)
cv2.imshow("dst2 - increate contrast", dst2)
cv2.imshow("dst3 - decreate contrast using average", dst3)
cv2.imshow("dst4 - increate contrast using average", dst4)
cv2.imwrite("dst.jpg", dst1)
cv2.waitKey(0)



