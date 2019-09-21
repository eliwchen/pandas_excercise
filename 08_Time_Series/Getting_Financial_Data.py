import pandas as pd
# package to extract data from various Internet sources into a DataFrame
# make sure you have it installed
from pandas_datareader import data, wb
# package for dates
import datetime as dt

index=pd.date_range("2015-01-01",pd.datetime.now().date())
stocks={"company":[" Apple", "Tesla", "Twitter", "IBM", "LinkedIn"],
        "price":[218.75,245.20,42.63,143.67,195.95],
        "volumn":[39763296,5313100,8059600,2206600,2506300]}
df=pd.DataFrame(stocks)
vol=df["volumn"]
print(type(df))
print(vol)
