import pandas as pd
# baby_names=pd.read_csv(r"https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv")
# baby_names.to_csv("baby_names",index=False)
baby_names=pd.read_csv("baby_names")
# print(baby_names.head(10))
# print(baby_names.drop(baby_names.columns[[0,1]],axis=1,inplace=True)) #删除第0列和1列 整数索引方式
# print(baby_names.drop([baby_names.columns[0],"Id"],axis=1,inplace=True)) #删除第0列和id列 整数加标签索引
del baby_names['Unnamed: 0'] #删除'Unnamed: 0'列
del baby_names['Id'] #删除'Id'列
print(baby_names.head(10))
# print(baby_names["Gender"].value_counts())
names=baby_names.groupby("Name").sum()
# print(baby_names["Name"].nunique())
df=names.sort_values("Count",ascending=False)["Count"]
print(df)
print(names[names.Count == names.Count.max()]) #count为最大值的姓名
print(len(names[names.Count == names.Count.min()])) #count为最小值的姓名总数
print(names[names.Count == names.Count.median()]) ##count为中位数的姓名
# print(df.median())
# print(df.describe())
