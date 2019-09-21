import pandas as pd
import datetime
crime=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv")
# print(crime.info())
crime["Year"]=pd.to_datetime(crime["Year"],format ="%Y")
# crime["Year"]=datetime.strftime(crime["Year"],"%Y-%m-%d")
print(crime.info())
print(crime.columns)
crime.index=crime["Year"]
crime.drop(["Total","Year"],axis=1,inplace=True)
print(crime.head())
crime=crime.resample("10AS").sum() #根据十年的频率进行采样
crime["Population"]=crime["Population"].resample("10AS").max()
print(crime.head())
print(crime.idxmax(0)) #返回同一列中最大值的索引
