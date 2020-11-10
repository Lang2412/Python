#-*- coding = utf-8 -*-
#@Time : 2020/10/29 15:05
#@Author : 冯朗
#@File ： test1-train_test_split().py
#@Software : PyCharm

import pandas as pd
from sklearn.model_selection import train_test_split

namelist = pd.DataFrame({
    #"number" : [0,1,2,3,4,5,6,7,8,9,10,11],
    "name" : ["suzuki","tanaka","yamada","watanabe","yamamoto","okada","ueda","inoue","hayashi","sato","hirayama","shimada"],
    "age": [30,40,55,29,41,28,42,24,33,39,49,53],
    "department" :  ["hr","legal","it","hr","hr","it","legal","legal","it","hr","legal","legal"],
    "attendance" : [1,1,1,0,1,1,1,0,0,1,1,1]
})

print(namelist)

namelist_train,namelist_test = train_test_split(namelist,test_size=0.3)     #划分训练集和测试集
print("----------train dataset----------t\n",namelist_train)                #输出训练集
print("----------test dataset----------t\n",namelist_test)                  #输出测试集
