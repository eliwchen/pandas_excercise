import pandas as pd
import random
import numpy as np
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
data1=pd.DataFrame(raw_data_1)
data2=pd.DataFrame(raw_data_2)
data3=pd.DataFrame(raw_data_3)
all_data=pd.concat([data1,data2],ignore_index=True)
print(all_data)
all_data_col=pd.concat([data1,data2],axis=1)
print(all_data_col)
# print(data3)
print(pd.merge(data1,data2,on="subject_id"))
print(pd.merge(data1,data2,on="subject_id",how="outer"))
