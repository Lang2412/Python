#-*- coding = utf-8 -*-
#@Time : 2020/10/26 16:00
#@Author : 冯朗
#@File ： test1-train_test_split().py
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
'''
# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
fig = plt.figure(figsize=(8,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
ax = plt.subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的实现
ax.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的虚线
ax.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# 设置横轴的上下限
xlim(-4.0,4.0)

# 设置横轴记号
xticks(np.linspace(-4,4,9,endpoint=True))

# 设置纵轴的上下限
ylim(-1.0,1.0)

# 设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))

# 以分辨率 72 来保存图片
savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
plt.show()





