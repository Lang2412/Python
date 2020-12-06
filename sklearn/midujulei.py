# coding=utf-8
# -*- coding = utf-8
"""
 @Time : 2020/12/6  19:19
 @Author : 冯朗
 @File ： midujulei.py
 @Software : PyCharm
"""

from sklearn.datasets.samples_generator import make_circles
import matplotlib.pyplot as plt

import time
from sklearn.cluster import KMeans

from sklearn.cluster import DBSCAN

X, y_true = make_circles(n_samples=1000, noise=0.15)  # 这是一个圆环形状的

plt.scatter(X[:, 0], X[:, 1], c=y_true)
plt.show()

# DBSCAN 算法
t0 = time.time()
dbscan = DBSCAN(eps=.1, min_samples=6).fit(X)  # 该算法对应的两个参数
t = time.time() - t0
plt.scatter(X[:, 0], X[:, 1], c=dbscan.labels_)
plt.title('time : %f' % t)
plt.show()