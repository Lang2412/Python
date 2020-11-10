#-*- coding = utf-8 -*-
#@Time : 2020/10/29 14:53
#@Author : 冯朗
#@File ： test_linalg.norm.py
#@Software : PyCharm

import numpy as np
x = np.array([[0,3,4],
             [1,6,4]])

print("矩阵整体元素的平方和开根号，不保留二维特征（默认参数）：",np.linalg.norm(x))
print("矩阵整体元素的平方和开根号，保留二维特征",np.linalg.norm(x,keepdims=True))

print("矩阵每个行向量求向量的 1 范数",np.linalg.norm(x,ord=1,axis=1,keepdims=True))
print("矩阵每个行向量求向量的 2 范数",np.linalg.norm(x,axis=1,keepdims=True))
print("矩阵每个列向量求向量的 2 范数",np.linalg.norm(x,axis=0,keepdims=True))

print("矩阵的 1 范数",np.linalg.norm(x,ord = 1,keepdims=True))
print("矩阵的 2 范数",np.linalg.norm(x,ord = 2,keepdims=True))
print("矩阵的 ∞ 范数",np.linalg.norm(x,ord = np.inf,keepdims=True))
