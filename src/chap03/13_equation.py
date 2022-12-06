import numpy as np, cv2

data = [ 3, 0, 6, -3, 4, 2, -5,-1, 9]
m1 = np.array(data, np.float32).reshape(3,3)
m2 = np.array([36, 10, 28], np.float32)

ret, inv = cv2.invert(m1, cv2.DECOMP_LU)                # 역행렬 계산
if ret:
    dst1 = inv.dot(m2)
    dst2 = cv2.gemm(inv, m2, 1, None, 1)
    ret, dst3 = cv2.solve(m1, m2, cv2.DECOMP_LU)

    print("[inv] = \n%s\n" % inv)
    print("[dst1] =", dst1.flatten())
    print("[dst2] =", dst2.flatten())
    print("[dst3] =", dst3.flatten())
else:
    print("역행렬이 존재하지 않습니다.")


