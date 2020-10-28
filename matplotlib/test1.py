#-*- coding = utf-8 -*-
#@Time : 2020/10/26 16:00
#@Author : 冯朗
#@File ： test1.py
#@Software : PyCharm

import matplotlib.pyplot as plt
import numpy as np
'''
fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)

x = np.linspace(0,np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)

ax1.plot(x,y_sin)
ax2.plot(x,y_sin,'go--',linewidth=2,markersize=5)
ax3.plot(x,y_cos,color='red',linestyle='-')
'''
'''
x = np.linspace(0,10,200)
data_obj = {'x': x,
            'y1': 2 * x + 1,
            'y2': 3 * x + 1.2,
            'mean': 0.5 * x * np.cos(2 * x) + 2.5 * x + 1.1}
fig,ax = plt.subplots()

#填充颜色
ax.fill_between('x','y1','y2',facecolor='yellow',data=data_obj)

ax.plot('x','mean',color='black',data = data_obj)
'''
'''
x = np.arange(10)
y = np.random.randn(10)
plt.scatter(x,y,color='blue',marker='*')
'''
'''
np.random.seed(1)
x = np.arange(5)
y = np.random.randn(5)

fig,axes = plt.subplots(ncols=2,figsize=plt.figaspect(.5))

#水平和竖直方向画条形图
vert_bars = axes[0].bar(x,y,color='blue',align='center')
horiz_bars = axes[1].barh(x,y,color='lightblue',align='center')
#水平和竖直方向画轴线
axes[0].axhline(0,color='black',linewidth=2)
axes[1].axvline(0,color='red',linewidth=2)
'''
np.random.seed(19680801)

n_bins = 10
x = np.random.randn(1000, 3)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

colors = ['red', 'tan', 'lime']
ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('bars with legend')

ax1.hist(x, n_bins, density=True, histtype='barstacked')
ax1.set_title('stacked bar')

ax2.hist(x,  histtype='barstacked', rwidth=0.9)

ax3.hist(x[:, 0], rwidth=0.9)
ax3.set_title('different sample sizes')

fig.tight_layout()

plt.show()





