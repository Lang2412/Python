# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

# Imports
import matplotlib.pyplot as plt
import numpy as np

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
plt.figure(figsize=(8,6), dpi=100)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的实线
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的虚线
plt.plot(X, S, color="green", linewidth=1.0, linestyle=":")

# 设置 x 轴范围
plt.xlim(-4.0,4.0)

# 设置 x轴 记号
plt.xticks(np.linspace(-4,4,9,endpoint=True))

# 设置 y 轴范围
plt.ylim(-1.0,1.0)

# 设置 y轴 记号
plt.yticks(np.linspace(-1,1,5,endpoint=True))

#保存图片到当前目录下
plt.savefig("exercice_2.png",dpi=72)

plt.show()
