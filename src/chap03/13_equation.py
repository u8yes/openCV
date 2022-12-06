import numpy as np, cv2

data = [ 3, 0, 6, -3, 4, 2, -5,-1, 9]
m1 = np.array(data, np.float32).reshape(3,3)
m2 = np.array([36, 10, 28], np.float32)

# 역행렬 계산
ret, inv = cv2.invert(m1, cv2.DECOMP_LU)
# decomposition(분해) # DECOMP_LU 는 디폴트 옵션
if ret: # 역행렬이 존재할 경우
    dst1 = inv.dot(m2) # 넘파이에 의한 m2 내적을 곱함.
    dst2 = cv2.gemm(inv, m2, 1, None, 1) # cv에 의한 내적 계산.
    ret, dst3 = cv2.solve(m1, m2, cv2.DECOMP_LU)
    # 연립방정식에 대한 풀이 결과

    print("[inv] = \n%s\n" % inv)
    print("[dst1] =", dst1.flatten())
    print("[dst2] =", dst2.flatten())
    print("[dst3] =", dst3.flatten())
else:
    print("역행렬이 존재하지 않습니다.")


