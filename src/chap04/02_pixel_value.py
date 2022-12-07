import numpy as np, cv2

image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

(x, y), (w, h) = (180, 37), (15, 10)
# x는 180위치에 y는 37위치에 시작포인트로 잡아줌.
# x는 15px만큼 접근해가겠다. y는 10px만큼 접근해가겠다는 것.

roi_img = image[y:y+h, x:x+w]
# [주의] 관심영역roi는 행은 y, 열은 x이다. 바뀌어서 표현.

print("[roi_img] = ")
for row in roi_img:
    for p in row:
        print("%4d" % p, end='')
    print() # 줄바꿈 - 행 단위로 출력

cv2.rectangle(image, (x, y, w, h), 255, 1) # 사각형
cv2.imshow("image", image)
cv2.waitKey(0)






