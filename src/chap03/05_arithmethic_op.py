import numpy as np, cv2

m1 = np.full((3, 6), 10, np.uint8)
m2 = np.full((3, 6), 50, np.uint8)
m_mask = np.zeros(m1.shape, np.uint8)
m_mask[ :, 3: ] = 1 # ROI - Region Of Interest 관심영역을 통해 강조

m_add1 = cv2.add(m1, m2)
m_add2 = cv2.add(m1, m2, mask=m_mask)
# mask 부분의 이미지를 더 강조하겠다는 것(밝은색)

# 행렬 나눗셈 수행
m_div1 = cv2.divide(m1, m2) # 정수형으로 나누기, 그래서 0
m1 = m1.astype(np.float32)
m2 = np.float32(m2)
m_div2 = cv2.divide(m1, m2)

titles = ['m1', 'm2', 'm_mask','m_add1','m_add2','m_div1', 'm_div2']
for title in titles:
    print("[%s] = \n%s \n" % (title, eval(title)))