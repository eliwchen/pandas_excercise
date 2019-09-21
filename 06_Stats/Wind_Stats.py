import pandas as pd
import datetime
data=pd.read_table("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data",
                   sep="\s+",parse_dates=[[0,1,2]])
#"\s+"任意空白字符分割；将0 1 2列解析为日期格式并合并

# data.to_csv("data",index=False)
# data=pd.read_csv("data",sep=" ")

# function that uses datetime
# def fix_century(x):
#     if x.year > 1989
#         year = x.year - 100
#     else:
#         x=x.year
#     return datetime.date(year, x.month, x.day)
def fix_century(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)
# apply the function fix_century on the column and replace the values to the right ones
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)
data['Yr_Mo_Dy']=pd.to_datetime(data['Yr_Mo_Dy'])
# print(data.info())
data = data.set_index('Yr_Mo_Dy') #列转化为索引，可以多层级索引
# data = data.set_index(['Yr_Mo_Dy',"RPT"]) #列转化为索引，可以多层级索引
# print(data)
# print(data.isnull()) #查看空值情况
# print(data.isnull().sum()) #统计每列空值数
# print(data.isnull().sum().sum()) #统计全部空值数
# print(data.isnull().sum()) #统计每列空值数
# print(len(data)-data.isnull().sum()) #统计每列非空值数
# print(data.notnull().sum()) #统计每列非空值数
# print((len(data)-data.isnull().sum()).sum()) #统计总非空值数
# print(data.mean().mean()) #计算总平均数
print(data.fillna(0).values.flatten().mean()) #计算总平均数;flatten函数将所有数据整理为一维
print(data.agg(["min","max","mean","std"]))#统计每列最小值、最大值、均值、标准差
print(data.describe())
# loc_stats=pd.DataFrame({"min":data.fillna(0).values.flatten().min(),"max":data.fillna(0).values.flatten().max(),
#                         "mean":data.fillna(0).values.flatten().mean(),
#                         "std":data.fillna(0).values.flatten().std()},index=0)
# print(loc_stats)
day_stats = pd.DataFrame()

# this time we determine axis equals to one so it gets each row.
day_stats['min'] = data.min(axis = 1) # min
day_stats['max'] = data.max(axis = 1) # max
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations
#
# print(day_stats.head())
# print(data)
print(data[data.index.month==1].mean())
print(data.resample("1A").mean()) #按一年频率采样
# data.groupby(data.index.to_period('A')).mean() #按一年频率采样2
print(data.resample("1M").mean()) #按一月频率采样
# data.groupby(data.index.to_period('M')).mean() #按一月频率采样2
print(data.resample("1W").mean()) #按一周频率采样
# data.groupby(data.index.to_period('W')).mean() #按一周频率采样2
weekly = data.resample('W').agg(['min','max','mean','std'])
print(weekly)
