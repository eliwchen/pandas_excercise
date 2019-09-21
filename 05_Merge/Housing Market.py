import pandas as pd
import random
import numpy as np
series1=pd.Series(np.random.randint(1,4,100))
series2=pd.Series(np.random.randint(1,3,100))
series3=pd.Series(np.random.randint(10000,30000,100))
df=pd.concat([series1,series2,series3],axis=1)
# print(df)
# df.columns=["bedrs","bathrs", "price_sqr_meter"] #重命名列方法1
df.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True) #重命名列方法2
print(df)
bigcolumn=pd.concat([series1,series2,series3])
print(bigcolumn)
# bigcolumn=pd.concat([series1,series2,series3],ignore_index=True) #在合并连接中忽略索引，合并后生成新索引
# print(bigcolumn)
bigcolumn.reset_index(drop=True, inplace=True)
print(bigcolumn)
