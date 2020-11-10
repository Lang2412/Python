# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5), dpi=80)
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的实线
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的虚线
plt.plot(X, S, color="red", linewidth=2.5, linestyle=":")

# 设置x轴范围
plt.xlim(X.min()*1.1, X.max()*1.1)

#设置x轴上的标记，并使用字符 π 进行替换
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# 设置y轴范围
plt.ylim(C.min()*1.1,C.max()*1.1)

plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

plt.show()
