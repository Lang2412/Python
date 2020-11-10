#-*- coding = utf-8 -*-
#@Time : 2020/10/29 15:38
#@Author : 冯朗
#@File ： tes1-counter().py
#@Software : PyCharm

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
