# coding=utf-8
# -*- coding = utf-8
"""
 @Time : 2020/11/26  14:07
 @Author : 冯朗
 @File ： PCA.py
 @Software : PyCharm
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.seterr(divide='ignore',invalid='ignore')

from sklearn.datasets.samples_generator import make_blobs
'''X作为样本特征，Y为样本簇类别，共1000个样本，每个样本三个特征，共四个簇'''
X,y = make_blobs(n_samples=1000,n_features=3,centers=[[3,3,3],[0,0,0],[1,1,1],[2,2,2]],
                 cluster_std=[0.2,0.1,0.2,0.2],random_state=9)
fig = plt.figure(1)
ax = Axes3D(fig,rect=[0,0,1,1],elev=30,azim=20)
plt.scatter(X[:,0],X[:,1],X[:,2],marker='o')

'''先不降维，只对数据进行投影，看看投影后的三个维度的方差分析'''
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print('----------------------------')

'''从三维降到二维'''
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print('----------------------------')
'''转化后的分布数据图'''
fig = plt.figure(2)
X_new = pca.transform(X)
plt.scatter(X_new[:,0],X_new[:,1],marker='o')
plt.show()

'''不直接指定降低的维度，指定降维后的主成分的方差和比例'''
pca = PCA(n_components=0.95)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print(pca.n_components_)
print('----------------------------')

pca = PCA(n_components=0.99)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print(pca.n_components_)
print('----------------------------')