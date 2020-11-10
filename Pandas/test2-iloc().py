#-*- coding = utf-8 -*-
#@Time : 2020/10/29 15:22
#@Author : 冯朗
#@File ： test2-iloc().py
#@Software : PyCharm

import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(16).reshape((4,4)),index= list(range(4)),columns=['a','b','c','d'])

print(df)

print(df.iloc[:3,[0,1,-1]])    #iloc函数为提取函数，用来提取数据，两个参数分别为 第几行 和 第几列
                                # （此处，取除了第3行外所有行，第0列，第1列和倒数第1列