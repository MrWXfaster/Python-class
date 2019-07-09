import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20160101',periods = 6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
'''以dates定义行，colums定义列，有名称的数据'''
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
'''不指定行和列，就会默认从0开始'''
print(df1)

df2 = pd.DataFrame({'A':1,'B':pd.Timestamp('20130102'),"C":pd.Series(1,index=list(range(4)),dtype='float32')})
print(df2)

print(df2.dtypes)

print(df2.index)
