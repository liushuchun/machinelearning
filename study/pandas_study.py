# coding: utf-8

from pandas import Series, DataFrame
import pandas as pd

'''
两大数据结构:
Series
DataFrame

Series 类似于一维数组，和数据标签（索引）
'''
obj = Series([4, 7, -5, 3])
print obj

# 索引在左边，值在右边. 可以通过values,index属性获取其数组表示形式和索引对象

print obj.values, obj.index

# 与普通numpy相比，你可以通过索引方式选取Series中的单个或一组值

obj2 = Series([4, 5, 6, 7], index=['d', 'b', 'a', 'c'])

print obj2

print "obj2.index:", obj2

print obj2['a']

print obj2['d']


'''
列数据的获取
'''

'''
DataFrame.as_matrix(columns=None)
'''


import pandas as pd
data1 = pd.DataFrame(...)  # 任意初始化一个列数为3的DataFrame
data1.columns = ['a', 'b', 'c']

1.
data1['b']
# 这里取到第2列（即b列）的值

2.
data1.b
# 效果同1，取第2列（即b列）
# 这里b为列名称，但必须是连续字符串，不能有空格。如果列明有空格，则只能采取第1种方法

3.
data1[data1.columns[1:]]
# 这里取data1的第2列和第3列的所有数据

番外1.
data1[5:10]
# 这里取6到11行的所有数据，而不是列数据

番外2.
data_raw_by_tick[2]
# 非法，返回“KeyError: 2”
