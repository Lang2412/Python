#-*- coding = utf-8 -*-
#@Time : 2020/11/3 15:12
#@Author : 冯朗
#@File ： Fit2.py
#@Software : PyCharm

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

# 目标函数
def real_func(x):
    return np.sin(2 * np.pi * x)

# 多项式
def fit_func(p,x):
    f = np.poly1d(p)
    return f(x)

# 残差
def residuals_func(p,x,y):
    ret = fit_func(p,x) - y
    return ret

# 十个点
x = np.linspace(0,1,10)
x_points = np.linspace(0,1,100)
print(x)

# 正态分布噪音的目标函数值
y_ = real_func(x)
y = [np.random.normal(0,0.1) + y1 for y1 in y_]
print(y)

def fitting(M=0):
    # 随机初始化多项式参数
    p_init = np.random.rand(M+1)
    p_lsq = leastsq(residuals_func,p_init,args=(x,y))
    print('Fitting Parameters:',p_lsq[0])

    # 画图
    plt.plot(x_points,real_func(x_points),label='real')
    plt.plot(x_points,fit_func(p_lsq[0],x_points),label='fitted curve')
    plt.plot(x,y,'bo',label='noise')
    plt.legend()    #绘制图例
    plt.show()
    return p_lsq

p_lsq_0 = fitting(M=3)