import pandas as pd
import random
import numpy as np
car1=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv")
car2=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv")
# print(car1.head())
car1.dropna(how="all",axis=1,inplace=True)
# print(car1.head())
print(car1.shape,car2.shape)
# print(car1.columns)
# print(car2.columns)
# print(car1.info(),car2.info())
car=pd.concat([car1,car2])
print(car.info())
owners=pd.Series(data=np.random.randint(15000,17000,len(car)))
print(owners)
car["owners"]=owners
print(car)
