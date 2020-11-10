#-*- coding = utf-8 -*-
#@Time : 2020/10/29 14:39
#@Author : 冯朗
#@File ： test2_twinx().py
#@Software : PyCharm

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fig,ax1 = plt.subplots()
# twinx()函数添加一个 Y 轴， twiny()函数可以添加 X 轴
ax2 = ax1.twinx()       #添加新的坐标轴，即双y轴
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data',color='g')
ax2.set_ylabel('Y2 data',color='b')

plt.show()