[TOC]

#	matplotlib

## 1.基本使用

```python
import matplotlib.pyplot as plt
```

在绘图结构中，figure创建画板窗口，subplot创建子图。所有的绘画只能在子图上进行。plt表示当前子图，若没有就创建一个子图。

**figure函数**:	画板，所有图像都是位于figure对象中，一个图像只能有一个figure对象。

```python
fig = plt.figure()		#生成画板
```

**subplot函数**：创建axes子图，figure对象下创建一个或多个subplot对象(即axes)用于绘制图像。

```python
ax1 = fig.add_subplot(221)		#生成2*2的画板,ax1 位于画板的第1行第1列
ax2 = fig.add_subplot(222)		#ax2位于画板的第2行第2列
ax3 = fig.add_subplot(223)
```

**plot函数**:  画出一系列的点，并且用线将它们连接起来。

###  配置参数

axes: 子图，设置坐标轴边界和表面的颜色、坐标刻度值大小和网格的显示
 figure: 控制dpi、边界颜色、图形大小、和子区( subplot)设置
 font: 字体集（font family）、字体大小和样式设置
 grid: 设置网格颜色和线性
 legend: 设置图例和其中的文本的显示
 line: 设置线条（颜色、线型、宽度等）和标记
 patch: 是填充2D空间的图形对象，如多边形和圆。控制线宽、颜色和抗锯齿设置等。
 savefig: 可以对保存的图形进行单独设置。例如，设置渲染的文件的背景为白色。
 verbose: 设置matplotlib在执行期间信息输出，如silent、helpful、debug和debug-annoying。
 xticks和yticks: 为x,y轴的主刻度和次刻度设置颜色、大小、方向，以及标签大小。



## 2.绘制2D图

### 2.1线性图

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)

x = np.linspace(0,np.pi)		#设置x取值范围（0,pi)，利用了numpy库
y_sin = np.sin(x)				
y_cos = np.cos(x)

ax1.plot(x,y_sin)				#绘制第1行第1列的子图
ax2.plot(x,y_sin,'go--',linewidth=2,markersize=5)	#利用一些参数来改变线
ax3.plot(x,y_cos,color='red',marker='+',linestyle='dashed')

plt.show()						
```

绘制效果如图所示：	![image-20201027203914090](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201027203914090.png)

|  线条风格  linestyle  | 描述       |
| :-------------------: | ---------- |
|          '-'          | 实线       |
|          ':'          | 虚线       |
|         '--'          | 破折线     |
| 'None'      ,     ' ' | 什么都不画 |
|         '-.'          | 点划线     |

```python
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
```

![image-20201028194839932](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201028194839932.png)

```python
import matplotlib.pyplot as plt
import numpy as np

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
```

![image-20201028200149209](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201028200149209.png)

```python
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)

ax.spines['right'].set_color('none')      #设置子图右边框为无色
ax.spines['top'].set_color('none')        #设置子图上边框为无色
ax.xaxis.set_ticks_position('bottom')     #设置x轴数据显示在底边框上
ax.spines['bottom'].set_position(('data',0))     #设置子图底边框的位置
ax.yaxis.set_ticks_position('left')       #设置y轴数据显示左边框上
ax.spines['left'].set_position(('data',0))       #设置子图左边框的位置

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

#添加label关键字，用来表示图例的名字
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-",label="cosine")	
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-",label="sine")	


plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(C.min()*1.1,C.max()*1.1)
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
#添加图例
plt.legend(loc='upper left', frameon=False)

plt.show()
```

![image-20201028204650196](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201028204650196.png)



此外，可以关键字参数来画图，即设置一个data关键字，所有需要的数据直接从data中寻找。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,200)		#设置范围

#设置关键字data_obj
data_obj = {'x': x,			
            'y1': 2 * x + 1,
            'y2': 3 * x + 1.2,
            'mean': 0.5 * x * np.cos(2 * x) + 2.5 * x + 1.1}

fig,ax = plt.subplots()			#设置画板和子图，两步可以同时进行

#填充颜色,fill_bwtween()是填充函数
ax.fill_between('x','y1','y2',facecolor='yellow',data=data_obj)

ax.plot('x','mean',color='black',data = data_obj)

```

**fill_bwtween()函数**:  填充函数，将选中的数据块进行填充。其中用到的几个参数：

`x`: 第一个参数为覆盖的区域的**横坐标轴范围**

`y1`:第二个参数为覆盖区域的**纵坐标轴的下限**

`y2`:第三个参数为覆盖区域的**纵坐标轴的上线**

`facecolor`:第四个参数为覆盖区域的**颜色**

`data`:第五个参数为放进来的**数据集对象**

![image-20201027205756510](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201027205756510.png)

### 2.2散点图

```python
x = np.arange(10)		
y = np.random.randn(10)			#随机取值
plt.scatter(x,y,color='blue',marker='*')	#marker关键字设置散点的标记
plt.show()
```

![image-20201027210452858](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201027210452858.png)

**scatte()函数**：绘制散点图

### 2.3条形图

```python
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
```

**figaspect()**函数：设置画布的高和宽之比,必须有参数，（.5）为0.5，即 高/宽 = 0.5。

**bar()函数**：绘制水平方向（坐标轴水平）条形图

**barh()函数**： 绘制竖直方向（坐标轴竖直）条形图

![image-20201027214931877](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201027214931877.png)