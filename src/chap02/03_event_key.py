import numpy as np
import cv2

# switch case 문을 dictionary으로 구현
switch_case = {
    ord('a'):"a키 입력", # ord() 함수 - 문자를 아스키코드로 변환
    ord('b'):"b키 입력",
    0x41:'A키 입력',
    int('0x42', 16):'B키 입력', # 문자열 데이터를 16진수로
    
}