import pandas as pd
##########pandas_exercises.01_getting and knowing your data#########
# chipo=pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")
chipo=pd.read_csv("chipo",usecols=[1,2,3,4,5]) #导入数据，取需要的列
# chipo=pd.read_csv("chipo")
# chipo.drop(chipo.columns[0],axis=pandas_exercises,inplace=True) #全部导入数据，删除不需要的列
pd.set_option('display.max_columns', None) #显示所有列
# print(chipo.head(10)) #查看前10行
chipo2=chipo.loc[:,["order_id","quantity","item_name","item_price"]]
print(chipo2.head(10)) #查看前10行
# chipo.to_csv("chipo")
# print(len(chipo)) #查看几行
# print(chipo.info()) #查看dataframe信息
# print(chipo.describe()) #dataframe简单描述统计
# print(len(chipo.index)) #查看行数
# print(len(chipo.columns)) #查看列数
# print(list(chipo.columns)) #查看所有列名
# print(chipo.index) #查看所有行索引
# print(chipo2.groupby("item_name")["item_name","quantity"].sum().sort_values(["quantity"],ascending=False)) #查看各品项订购情况
# print(chipo.groupby("choice_description")["choice_description","quantity"].sum().sort_values(["quantity"],ascending=False))
# print(len(chipo2.groupby("item_name")["item_name"])) #查看品项种类数
# print(chipo["quantity"].sum())
# print(chipo2["item_price"].dtypes) #查看数据类型
# chipo2["item_price"]=chipo2["item_price"].apply(lambda x: float(x[pandas_exercises:-pandas_exercises])) #数据转换方法1
chipo2["item_price"]=chipo2["item_price"].apply(lambda x: x.replace("$",""))#数据转换方法2.pandas_exercises
chipo2["item_price"]=chipo2["item_price"].astype("float64")#数据转换方法2.2
# print(chipo2["item_price"].dtypes)
# print(chipo2.head(5)) #查看前5行
# revenue=sum(chipo2["item_price"]*chipo2["quantity"]) #查看总收入
# print(revenue)
# order_id_count=len(chipo2.groupby("order_id")["order_id"])
# print(order_id_count) #查看订单数
# revenue_perorder=revenue/order_id_count
# print(revenue_perorder)
# print(len(chipo2.groupby("item_name")["item_name"].count()))  # 查看品项种类数
# print(chipo2["item_name"].value_counts())

##########2.flitering and sorting #########
# print(chipo2.loc[:,["item_name","item_price"]]) #查看每个品项的价格
# print(chipo2.groupby("item_name")["item_price"].min()) #查看每个品项的最低价格
# print(chipo2.sort_values(by="item_name",ascending=False)) #查看单价最高的商品
# print(chipo2.sort_values(by="item_price",ascending=False)) #查看单价最高的商品
# print(chipo2.groupby("item_name").sum().sort_values(by="item_price",ascending=False))
# print(len(chipo2[chipo2["item_name"].isin(["Veggie Salad Bowl"])])) #Veggie Salad Bowl的订购次数
print(len(chipo[chipo["item_name"] == "Veggie Salad Bowl"])) #Veggie Salad Bowl的订购次数
# print(len(chipo2[(chipo2["item_name"].isin(["Canned Soda"]))&(chipo2["quantity"]>pandas_exercises)])) #Canned Soda订购量超过1的订购次数
