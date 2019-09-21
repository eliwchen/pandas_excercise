import pandas as pd
# users=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep="|",index_col="user_id")
# users.to_csv("users")
users=pd.read_csv("users",index_col="user_id")
# print(users.head(25))
# print(users.tail(10))
# print(users.info())
# print(users.columns)
# print(users.index)
# print(users.dtypes)
# print(users["occupation"])
# print(len(users.groupby("occupation")["occupation"]))#职业的种类数solution1
print(users["occupation"].nunique()) #职业的种类数solution2
print(users["occupation"].unique()) #职业的种类(调取唯一值)
# print(users.groupby("occupation")["occupation"].count().sort_values(ascending=False).head(pandas_exercises))#统计从事各occupation人数 solution1
print(users["occupation"].value_counts().head(1)) #统计从事各occupation人数 solution2
# print(users.describe())#默认只描述统计数值型的列
# print(users.describe(include="all")) #描述统计所有列
print(users["occupation"].describe()) #只描述统计occupation
# print(users["age"].mean())
# print(users.groupby("age")["age"].count().sort_values(ascending=True).head(5))
