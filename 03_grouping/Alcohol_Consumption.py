import pandas as pd
# drinks=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv")
# drinks.to_csv("drinks",index=False) #不写入索引列
drinks=pd.read_csv("drinks")
print(drinks.columns)
# print(drinks.info())
# print(drinks.describe())
# print(drinks.head())
# print(drinks.groupby("continent")["beer_servings"].mean().sort_values(ascending=False)) #各大洲啤酒消费均值
# print(drinks.groupby("continent")["wine_servings"].describe()) #各大洲红酒消费各项数值
# print(drinks.groupby("continent").mean()) #各大洲酒品消费均值
# print(drinks.groupby("continent").median()) #各大洲酒品消费中位数
# df=drinks.groupby("continent")["spirit_servings"].describe()
# print(df[["mean","min","max"]]) #各大洲spirit消费均值、最大值与最小值
print(drinks.groupby("continent")["spirit_servings"].agg(['mean', 'min', 'max'])) #从0.20.1开始，pandas引入了agg函数，它提供基于列的聚合操作


