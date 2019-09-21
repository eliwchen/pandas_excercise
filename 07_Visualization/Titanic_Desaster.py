#######模块导入
import pandas as pd
import collections
import matplotlib.pyplot as plt

###### 解决中文字体显示问题
font = {'family' : 'SimHei'}
plt.rc('font', **font)

#####数据准备
# titanic=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv")
# titanic.to_csv("titanic",index=False)
titanic=pd.read_csv("titanic")
print(titanic.head())
