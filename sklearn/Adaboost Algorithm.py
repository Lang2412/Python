# coding=utf-8
# -*- coding = utf-8
"""
 @Time : 2020/11/26  14:11
 @Author : 冯朗
 @File ： Adaboost Algorithm.py
 @Software : PyCharm
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#data
def create_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['label'] = iris.target
    df.columns = ['speal length', 'speal width', 'petal length', \
                  'petal width', 'label']
    data = np.array(df.iloc[:100, [0, 1, -1]])
    for i in range(len(data)):
        if data[i, -1] == 0:
            data[i, 1] = -1
        print(data)
        return data[:, :2], data[:, -1]

X, y = create_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

plt.scatter(X[:50, 0], X[:50, 1], label='0')
plt.scatter(X[50:, 0], X[50:, 1], label='1')
plt.legend()

class AdaBoost:
    def __init__(self,n_estimeators=50,learning_rate=1.0):
        self.clf_num = n_estimeators
        self.learning_rate = learning_rate

    def init_args(self,datasets,labels):
        self.X = datasets
        self.Y = labels
        self.M, self.N = datasets.shape

        #弱分类器数目和合集
        self.clf_num = []

        #初始化weights
        self.weights = [1.0/self.M] * self.M

        #G(x)系数alpha
        self.alpha = []

    def _G(self, features, labels, weights):
        m = len(features)
        error = 10000.0
        best_v = 0.0
        #单维features
        features_min = min(features)
        features_max = max(features)
        # // 是取整除符号，为向下取整
        n_step = (features_max - features_min + self.learning_rate) // self.learning_rate
        print('n_step:{}'.format(n_step))
        direct,compare_array = None,None
        for i in range(1,int(n_step)):
            v = features_min + self.learning_rate * i

            if v not in features:
                # 误分类计算
                compare_array_positive = np.array([1 if features[k] > v else -1 for k in range(m)])
                weight_error_positive = sum([weights[k] for k in range(m) \
                                             if compare_array_positive[k] != labels[k]])

                compare_array_nagetive = np.array([-1 if features[k] > v else 1 for k in range(m)])
                weight_error_nagetive = sum([weights[k] for k in range(m) \
                                             if compare_array_nagetive[k] != labels[k]])

                if weight_error_positive < weight_error_nagetive:
                    weight_error = weight_error_positive
                    _compare_array = compare_array_positive]
                    direct = 'positive'
                else:
                    weight_error = weight_error_nagetive
                    _compare_array = compare_array_nagetive
                    direct = 'nagetive'
                print('v:{}     error:{}'.format(v,weight_error))
                if weight_error < error:
                    error = weight_error
                    compare_array = _compare_array
                    best_v = v
        return best_v,direct,error,compare_array

    #计算alpha
    def _alpha(self,error):
        return 0.5 * np.log((1-error)/error)

    #规范化因子
    def _Z(self,weights,a,clf):
        return sum([weights[i] * np.exp(-1 * a * self.Y[i] * clf[i]) for i in range(self.M)])

    #权值更新

