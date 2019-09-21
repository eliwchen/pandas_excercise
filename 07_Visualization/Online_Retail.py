#######模块导入
import pandas as pd
import collections
import matplotlib.pyplot as plt

###### 解决中文字体显示问题
font = {'family' : 'SimHei'}
plt.rc('font', **font)

#####数据准备
# online_rt=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv",encoding = 'latin1')
# online_rt.to_csv("online_rt",index=False)
online_rt=pd.read_csv("online_rt")
online_rt["Revenue"]=online_rt.Quantity*online_rt.UnitPrice
print(online_rt.columns)
# print(online_rt.head())
df=online_rt[(online_rt.Country != "United Kingdom") & (online_rt.Quantity>0)].groupby("Country")["Quantity"].sum().sort_values(ascending=False).head(10)
# print(df.head(3))

df_average=online_rt.groupby(["Country","CustomerID"])["UnitPrice"].mean() #groupby 两层

# df_average.groupby("CustomerID")["UnitPrice"].mean()
print(df_average.head())

df_Netherlands =online_rt[(online_rt.Country == "Netherlands") & (online_rt.Quantity>0)]
df_Netherlands2=df_Netherlands.groupby("CustomerID")[["Quantity","UnitPrice"]].mean()
df_EIRE=online_rt[(online_rt.Country == "EIRE") & (online_rt.Quantity>0)]
df_EIRE2=df_EIRE.groupby("CustomerID")[["Quantity","UnitPrice"]].mean()
df_Germany=online_rt[(online_rt.Country == "Germany") & (online_rt.Quantity>0)]
df_Germany2=df_Germany.groupby("CustomerID")[["Quantity","UnitPrice"]].mean()

#######数据可视化
plt.subplot(211)
plt.bar(df.index,df)
plt.xticks(fontsize=0.5,rotation=90,fontproperties = 'Times New Roman')

plt.subplot(212)
plt.scatter(df_Netherlands2["UnitPrice"],df_Netherlands2["Quantity"])
plt.scatter(df_EIRE2["UnitPrice"],df_EIRE2["Quantity"])
plt.scatter(df_Germany2["UnitPrice"],df_Germany2["Quantity"])
plt.legend(["Netherlands","EIRE","Germany"],prop={'family' : 'Times New Roman', 'size':10})

plt.tight_layout(pad=2,rect=(0,0,1,1)) #设置两个子图之间的间隔，rect是图表的位置，默认（0，0，1，1）
plt.show()
