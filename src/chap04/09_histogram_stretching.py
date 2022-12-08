import numpy as np, cv2
from Common.histogram import draw_histo

def search_value_idx(hist, bias = 0): # bias라는 매개변수 선언(디폴트는 0으로)
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)
        # 움직이면서 한칸씩 상승(bias가 0) or 하강(bias가 1)하면서 최소, 최대값 찾아냄
        if hist[idx] > 0:
            return idx
    return -1

image = cv2.imread("dst.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

bsize, ranges = [64], [0, 256] # size를 64개, 256/64하면 '4'가 나옴.
hist = cv2.calcHist([image], [0], None, bsize, ranges)
# channel(BGR)값이 흑백일 때 0번 채널은 BLUE

bin_width = ranges[1] / bsize[0]
high = search_value_idx(hist, bsize[0] - 1) * bin_width # 최대값
low = search_value_idx(hist, 0) * bin_width # 최소값

idx = np.arange(0,256)
idx = (idx - low) * 256 / (high - low) # 정규화의 기본 개념에서 255로 펼쳐줌
idx[0:int(low)] = 0
idx[int(high+1):] = 255

dst = cv2.LUT(image, idx.astype('uint8')) # LookUp Table 사용
# 최소, 최대값을 찾아서 0~255사이로 펼쳐주게끔 테이블로 만들어줌.
# dst - destination
# 현재는 dst가 스트레칭 되서 쫘악 퍼져있는 상태가 돼있음.
hist_dst = cv2.calcHist([dst],[0], None, bsize, ranges)

hist_img = draw_histo(hist, (200,360))
hist_dst_img = draw_histo(hist_dst, (200, 360))

print("high_value=", high)
print("low_value=", low)

cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)

cv2.imshow("dst", dst)
cv2.imshow("hist_dst_img", hist_dst_img)

cv2.waitKey(0)
