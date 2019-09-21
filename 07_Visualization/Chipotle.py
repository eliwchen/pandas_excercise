#######模块导入
import pandas as pd
import collections
import matplotlib.pyplot as plt

###### 解决中文字体显示问题
font = {'family' : 'SimHei'}
plt.rc('font', **font)

####数据准备
chipo=pd.read_table("chipo",sep=",")
chipo.drop("Unnamed: 0",axis=1,inplace=True)
print(chipo.head(10))
print(chipo.columns)
print(chipo.groupby("item_name")["quantity"].sum().sort_values(ascending=False).head(5))
df=chipo.groupby("item_name")["quantity"].sum().sort_values(ascending=False).head(5)
plt.style.use('ggplot') #使用'ggplot'风格美化显示的图表
df_price_quantity=chipo.groupby("item_price")["quantity"].sum().head(20)

#####数据可视化
# plt.style.use('ggplot') #使用'ggplot'风格美化显示的图表
plt.subplot(211)
plt.bar(df.index,df,width=0.8,color="gray")
plt.title("ItemName-Quantity",fontdict={'family' : 'Times New Roman', 'size'   : 16})
# plt.tick_params(labelsize=7) #设置刻度轴字体大小
plt.xticks(fontsize=7,rotation=360) #设置刻度轴字体大小方法2,刻度轴旋转
plt.subplot(212)
plt.scatter(df_price_quantity.index,df_price_quantity,s = 50, c = 'green')
plt.title("Price-Quantity")
plt.xticks(fontsize=5,) #设置刻度轴字体大小方法2
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.tight_layout(pad=2,rect=(0,0,1,1)) #设置两个子图之间的间隔，rect是图表的位置，默认（0，0，1，1）
plt.show()
