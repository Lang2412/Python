#-*- coding = utf-8 -*-
#@Time : 2020/11/2 20:31
#@Author : 冯朗
#@File ： test-iris.py
#@Software : PyCharm

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['label'] = iris.target
df.columns = ['speal length','speal width','petal length','petal width','label']

plt.scatter(df[:50]['speal length'],df[:50]['speal width'],label='0')
plt.scatter(df[50:100]['speal length'],df[50:100]['speal width'],label='1')
plt.xlabel('speal length')
plt.ylabel('speal width')
plt.legend()
plt.show()
