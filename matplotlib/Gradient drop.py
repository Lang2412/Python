#-*- coding = utf-8 -*-
#@Time : 2020/11/3 19:16
#@Author : 冯朗
#@File ： Gradient drop.py
#@Software : PyCharm

import numpy as np
import matplotlib.pyplot as plt

plot_x = np.linspace(-1,6,141)      #在-1到6之间等距离生成141个数
plot_y = (plot_x - 2.5) ** 2 + 3
plt.plot(plot_x,plot_y)
plt.show()

# 定义一个求二次函数的倒数的函数
def dJ(x):
    return 2*(x-2.5)

# 定义一个求y函数值的函数
def J(x):
    try:
        return (x -  2.5) ** 2 + 3
    except:
        return float('inf')

x = 0.0             #选择一个起始点
eta = 0.1           #学习率
epsilon = 1e-8      #用来判断是否达到二次函数的最小值的条件，1e-8是10的负8次方
history_x = [x]     #用来记录使用梯度下降法走过的x坐标
while True:
    gradient = dJ(x)
    last_x = x
    x = x - eta * gradient
    history_x.append(x)

    if (abs(J(last_x) - J(x)) < epsilon):
        break

print(history_x)
plt.plot(plot_x,plot_y)
plt.plot(np.array(history_x),J(np.array(history_x)),color='r',marker='*')
plt.show()
