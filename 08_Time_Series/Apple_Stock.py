import pandas as pd
import seaborn as sns
import  matplotlib.pyplot as plt
apple=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv")
apple["Date"]=pd.to_datetime(apple["Date"])
# print(apple.info())
apple.index=apple["Date"]
apple.drop("Date",axis=1,inplace=True)
# print(apple.index.duplicated())
print(apple.index.is_unique)
apple.sort_values(by="Date",ascending=True,inplace=True)
print(apple)
apple_month = apple.resample('BM').mean()
print(apple_month.head())
print(len(apple.resample("1M").mean())) #计算月数
print((apple.index.max() - apple.index.min()).days) #计算时间跨度
# print(apple.columns)
# plt.figure(figsize=(13.5,9))
# plt.plot(apple["Adj Close"])
# plt.show()
