# NumPy

[TOC]

## 1.简介

NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：

- 一个强大的N维数组对象 ndarray
- 广播功能函数
- 整合 C/C++/Fortran 代码的工具
- 线性代数、傅里叶变换、随机数生成等功能



## 2.基础使用

### 2.1Ndarray对象

NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。

Ndarray对象是存放同类型元素的多维数组

Ndarray对象每个元素在内存中都有相同的存储大小的区域

Ndarray内容的存储：

- 一个指向数据（内存或内存映射文件中的一块数据）的指针

- 数据类型或 dtype，描述在数组中的固定大小值的格子

- 一个表示数组形状（shape）的元组，表示各维度大小的元组

- 一个跨度元组（stride），其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数

  ndarray内部结构示意图：![**image-20201102152549357**](C:\Users\疯狼\AppData\Roaming\Typora\typora-user-images\image-20201102152549357.png)

**创建ndarray对象**：调用array函数

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

**参数列表：**

| 名称   | 描述                                                      |
| :----- | :-------------------------------------------------------- |
| object | 数组或嵌套的数列                                          |
| dtype  | 数组元素的数据类型，可选                                  |
| copy   | 对象是否需要复制，可选                                    |
| order  | 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认） |
| subok  | 默认返回一个与基类类型一致的数组                          |
| ndmin  | 指定生成数组的最小维度                                    |

**实例：**

```python
>>> import numpy as np
>>> a = np.array([1,2,3])
>>> a
array([1, 2, 3])
```

```python
>>> import numpy as np
>>> a = np.array([[1,2],[3,4]])			#二维数组
>>> a
array([[1, 2],
       [3, 4]])
```

```python
>>> import numpy as np
>>> a = np.array([1,2,3,4,5],ndmin = 2)		#ndmin参数，设置最小维度为2
>>> a
array([[1, 2, 3, 4, 5]])
```

```python
>>> import numpy as np
>>> a = np.array([1,2,3],dtype = complex)		#dtype参数，设置参数类型为复数
>>> a
array([1.+0.j, 2.+0.j, 3.+0.j])
```

### 2.2 数据类型

numpy支持的数据类型比python内置的类型要多，基本可以和C的数据类型对应。

| 名称       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| bool_      | 布尔型数据类型（True 或者 False）                            |
| int_       | 默认的整数类型（类似于 C 语言中的 long，int32 或 int64）     |
| intc       | 与 C 的 int 类型一样，一般是 int32 或 int 64                 |
| intp       | 用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64） |
| int8       | 字节（-128 to 127）                                          |
| int16      | 整数（-32768 to 32767）                                      |
| int32      | 整数（-2147483648 to 2147483647）                            |
| int64      | 整数（-9223372036854775808 to 9223372036854775807）          |
| uint8      | 无符号整数（0 to 255）                                       |
| uint16     | 无符号整数（0 to 65535）                                     |
| uint32     | 无符号整数（0 to 4294967295）                                |
| uint64     | 无符号整数（0 to 18446744073709551615）                      |
| float_     | float64 类型的简写                                           |
| float16    | 半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位      |
| float32    | 单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位      |
| float64    | 双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位     |
| complex_   | complex128 类型的简写，即 128 位复数                         |
| complex64  | 复数，表示双 32 位浮点数（实数部分和虚数部分）               |
| complex128 | 复数，表示双 64 位浮点数（实数部分和虚数部分）               |

**数据类型对象（dtype)**:

- 数据的类型（整数，浮点数或者 Python 对象）
- 数据的大小（例如， 整数使用多少个字节存储）
- 数据的字节顺序（小端法或大端法):
  - 字节顺序是通过对数据类型预先设定 **<** 或 **>** 来决定的。 **<** 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。**>** 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。
- 在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
- 如果数据类型是子数组，那么它的形状和数据类型是什么。

```python
numpy.dtype(object, align, copy)
```

**参数列表：**

| 名称   | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| object | 要转换的数据类型的对象                                       |
| align  | 如果为 true，填充字段使其类似 C 的结构体。                   |
| copy   | 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用 |

```python
>>> import numpy as np
>>> dt = np.dtype(np.int32)
>>> dt
dtype('int32')
```

```python
>>> import numpy as np
#int8,int16,int32,int64,四种数据类型可以使用字符串'i1','i2','i4','i8'代替
>>> dt = np.dtype('i4')
>>> dt
dtype('int32')
```

```python
>>> import numpy as np
#创建结构化数据类型
>>> dt = np.dtype([('age',np.int8)])
#将结构化数据运用到ndarray对象
>>> a = np.array([(10,),(20,),(30,)],dtype = dt)
>>> print(dt,a)
[('age', 'i1')]  [(10,) (20,) (30,)]
>>> print(a['age'])			#类型字段名可以用于存取实际的age列
[10 20 30]
```

```python
>>> import numpy as np
>>> student = np.dtype([('name','S20'),('age','i4'),('marks','f4')])
>>> a = np.array([('abc',21,50),('xyz',18,75)],dtype = student)
>>> print(student)
[('name', 'S20'), ('age', '<i4'), ('marks', '<f4')]
>>> print(a)
[(b'abc', 21, 50.) (b'xyz', 18, 75.)]
```

**内置类型代码：**

| 字符 | 对应类型              |
| :--- | :-------------------- |
| b    | 布尔型                |
| i    | (有符号) 整型         |
| u    | 无符号整型 integer    |
| f    | 浮点型                |
| c    | 复数浮点型            |
| m    | timedelta（时间间隔） |
| M    | datetime（日期时间）  |
| O    | (Python) 对象         |
| S, a | (byte-)字符串         |
| U    | Unicode               |
| V    | 原始数据 (void)       |

### 2.3 Numpy数组属性

| 属性             | 说明                                                         |
| :--------------- | :----------------------------------------------------------- |
| ndarray.ndim     | 秩，即轴的数量或维度的数量。一维数组的秩为 1，二维数组的秩为 2，以此类推 |
| ndarray.shape    | 数组的维度，对于矩阵，n 行 m 列                              |
| ndarray.size     | 数组元素的总个数，相当于 .shape 中 n*m 的值                  |
| ndarray.dtype    | ndarray 对象的元素类型                                       |
| ndarray.itemsize | ndarray 对象中每个元素的大小，以字节为单位                   |
| ndarray.flags    | ndarray 对象的内存信息                                       |
| ndarray.real     | ndarray元素的实部                                            |
| ndarray.imag     | ndarray 元素的虚部                                           |
| ndarray.data     | 包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。 |

```python
>>>import numpy as np
>>> a =np.array([[1,2,3],[4,5,6]])
>>> a.shape = (3,2)			#调整数组的大小，将2行3列数组调整为3行2列
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
```

```python
>>>import numpy as np
>>> x = np.array([1,2,3,4,5],dtype = np.int8)		#数组的dtype为int8（1个字节）
>>> y = np.array([1,2,3,4,5],dtype = np.float64)	#数组的dtype为float64(8个字节)
>>> print(x.itemsize)
1
>>> print(y.itemsize)
8
```

**ndarray.flags**:返回ndarray对象的内存信息，有以下属性

| 属性             | 描述                                                         |
| :--------------- | :----------------------------------------------------------- |
| C_CONTIGUOUS (C) | 数据是在一个单一的C风格的连续段中                            |
| F_CONTIGUOUS (F) | 数据是在一个单一的Fortran风格的连续段中                      |
| OWNDATA (O)      | 数组拥有它所使用的内存或从另一个对象中借用它                 |
| WRITEABLE (W)    | 数据区域可以被写入，将该值设置为 False，则数据为只读         |
| ALIGNED (A)      | 数据和所有元素都适当地对齐到硬件上                           |
| UPDATEIFCOPY (U) | 这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新 |

```python
>>> import numpy as np
>>> x = np.array([1,2,3,4,5])
>>> print(x.flags)
  C_CONTIGUOUS : True
  F_CONTIGUOUS : True
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False
  UPDATEIFCOPY : False
```

