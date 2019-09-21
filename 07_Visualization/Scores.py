#######模块导入
import pandas as pd
import collections
import matplotlib.pyplot as plt

###### 解决中文字体显示问题
font = {'family' : 'SimHei'}
plt.rc('font', **font)

#####数据准备
df=pd.DataFrame({"first_name":["Jason","Molly","Tina","Jake","Amy"],
                 "last_name":["Miller","Jacobson","Ali","Milner","Cooze"],
                 "age":[42,52,36,24,73],
                 "female":[0,1,1,0,1],
                 "preTestScore":[4,24,31,2,3],
                 "postTestScore":[25,94,57,62,70]})
print(df.head())
######数据可视化
plt.subplot(211)
color={1:"pink",0:"blue"}
plt.scatter(df.index,df["preTestScore"],s=df["age"]*4.5, c=[color[i] for i in df.female],alpha=0.5)
plt.xlabel("Index")
plt.ylabel("PreTestScore")
plt.title("Scatter of PreTestScore")

plt.subplot(212)
plt.scatter(df.index,df["postTestScore"],s=df["age"]*4.5,c=df.female,alpha=0.5)
plt.xlabel("Index")
plt.ylabel("PostTestScore")
plt.title("Scatter of PostTestScore")

plt.tight_layout(pad=1,rect=(0,0,1,1)) #设置两个子图之间的间隔，rect是图表的位置，默认（0，0，1，1）
plt.show()
