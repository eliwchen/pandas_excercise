import pandas as pd
import numpy as np
df=pd.read_csv("https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv")
# df=df.set_index(df.Date)
df.Date=pd.to_datetime(df.Date)
df.index=df.Date
df.drop("Date",axis=1,inplace=True)
print(df.head(10))
print(df.info())
monthly=df.resample("M").sum()
monthly=monthly.replace(0,np.nan) #用np.nan替换0
monthly.dropna(how="any",inplace=True)
yearly=monthly.resample("Y").sum()
print(monthly)
print(yearly)
