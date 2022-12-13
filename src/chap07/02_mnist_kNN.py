import cv2, numpy as np
import os, gzip, pickle
from urllib.request import urlretrieve
# url을 통해 다운로드 가능하게 해주는 라이브러리
import matplotlib.pyplot as plt

def load_mnist(filename):
    if not os.path.exists(filename):
        print("Downloading...")
        link = "http://figshare.com/ndownloader/files/25635053"
        urlretrieve(link, filename)

    with gzip.open(filename, 'rb') as f:
        return pickle.load(f, encoding='latin1')

def graph_image(data, lable, title, nsample):
    plt.figure(num=title, figsize=(6, 9))
    rand_idx = np.random.choice(range(data.shape[0]), nsample)
    for i, id in enumerate(rand_idx):
        img = data[id].reshape(28, 28)
        plt.subplot(6, 4, i + 1), plt.axis('off'), plt.imshow(img, cmap='gray')
        plt.title('%s: %d' % (title , lable[id]))
    plt.tight_layout()

train_set, valid_set, test_set = load_mnist('mnist.pk1.gz')
# 압축 이미지 파일을 제공
train_data, train_label = train_set
test_data, test_label = test_set

# MNIST로드 데이터 크기 확인
print("train_set", train_set[0].shape)
print("valid_set", valid_set[0].shape)
print("test_set", test_set[0].shape)

print("training...")
knn = cv2.ml.KNearest_create() # KNearest_create는 학습을 시켜주는 기능.
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_label)

nsample = 100 # 100개의 샘플 데이터
print("%d개 prediction..." % nsample)

_, resp, _, _ = knn.findNearest(test_data[:nsample], k=5)
accur = sum(test_label[:nsample] == resp.flatten()) / len(resp)

print("정확도=", accur * 100, "%")
graph_image(train_data, train_label, 'label', 24)
graph_image(test_data[:nsample], resp, 'predict', 24)
plt.show()










