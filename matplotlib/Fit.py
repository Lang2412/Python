#-*- coding = utf-8 -*-
#@Time : 2020/11/3 14:52
#@Author : 冯朗
#@File ： Fit.py
#@Software : PyCharm

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

Xi = np.array([160,165,158,172,159,176,160,162,171])
Yi = np.array([58,63,57,65,62,66,58,59,62])

# 拟合函数func
def func(p,x):
    k,b = p
    return k * x + b

# 偏差函数
def error(p,x,y):
    return func(p,x) - y

# 设定k 和 b 的初值，任意设定，经过几次试验，发现p0的值会影响cost的值
p0 = [5,40]

# 把error函数中出了p0以外的参数打包到args中
Para = leastsq(error,p0,args=(Xi,Yi))

# 读取结果
k,b = Para[0]
print("k=",k,"b=",b)

# 绘制样本点
plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="green",label = "Sample Data",linewidths=2)

# 绘制拟合直线
x = np.linspace(150,190,100)    #在150-190之间画100个连续的点
y = k * x + b
plt.plot(x,y,color='red',label='Fitting Line',linewidth=2)
plt.legend()    #绘制图例
plt.show()
