import numpy as np
import cv2

# switch case 문을 dictionary으로 구현
switch_case = {
    ord('a'):"a키 입력", # ord() 함수 - 문자를 아스키코드로 변환
    ord('b'):"b키 입력",
    0x41:'A키 입력',
    int('0x42', 16):'B키 입력', # 문자열 데이터를 16진수로
    2424832:"왼쪽 화살표키 입력",    # 0x250000
    2490368:"윗쪽 화살표키 입력",    # 0x260000
    2555904:"오른쪽 화살표키 입력",   # 0x270000
    2621440:"아래쪽 화살표키 입력",   # 0x280000
}

image = np.ones((200,300), np.float64) # 화소값 200행, 300열
cv2.namedWindow('Keyboard Event')
cv2.imshow('Keyboard Event', image)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27:
        break       # ESC키 누르면 종료

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()