import numpy as np, cv2

def morphing():
    h, w = image.shape[:2]
    dst = np.zeros((h, w), image.dtype)
    ys = np.arange(0, image.shape[0], 1)
    xs = np.arange(0, image.shape[1], 0.1) # 0.1 단위로 저장

    x1, x10 = pt1[0], pt1[0] * 10
    ratios = xs / x1
    ratios[x10:] = (w - xs[x10:]) / (w-x1)

    dxs = xs + ratios * (pt2[0] - pt1[0])
    xs, dxs = xs.astype(int), dxs.astype(int)

    ym, xm = np.meshgrid(ys, xs)
    _, dxm = np.meshgrid(ys, dxs)
    dst[ym, dxm] = image[ym, xm]
    cv2.imshow("image", dst)


def onMouse(event, x, y, flags, param):
    global pt1, pt2
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x, y)
        morphing()
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        pt1 = pt2 = (-1, -1)
        cv2.imshow("image",image)


image = cv2.imread("07_images/warp.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

pt1 = pt2 = (-1, -1)
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
# 마우스 클릭할 때마다 onMouse의 함수를 호출해주게 됨.
cv2.waitKey(0)
