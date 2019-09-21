import pandas as pd
import xlrd
# users=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep="|")
# users.to_csv("users",index=False)
users=pd.read_csv("users")
print(users.columns)
# print(users.head())
# print(users.groupby("occupation")["age"].mean())
# df=users[users["gender"]=="M"]
# df1=df.groupby("occupation")["gender"].count()
# df2=users.groupby("occupation")["gender"].count()
# print((df1/df2).sort_values(ascending=False))
# print(users.groupby("occupation")["age"].agg(["min","max"]))
# print(pd.pivot_table(users,values="age",index="occupation",columns="gender",aggfunc="mean"))
# print(users.groupby(["occupation","gender"])["age"].mean()) #分层索引，分组
# occu_gender_count=pd.pivot_table(users,values="age",index="occupation",columns="gender",aggfunc="count",fill_value=0)
# print(pd.pivot_table(users,values="age",index="occupation",columns="gender",aggfunc="count",fill_value=0))
# create a data frame and apply count to gender
# gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
# print(gender_ocup)
# gender_ocup = users.groupby(['occupation', 'gender'])["gender"].count()
# create a DataFrame and apply count for each occupation
# occup_count = users.groupby(['occupation']).agg('count')
# print(occup_count)
# # divide the gender_ocup per the occup_count and multiply per 100
# # occup_gender = gender_ocup.div(occup_count, level = "occupation") * 100
# occup_gender = gender_ocup/occup_count * 100
# # present all rows from the 'gender column'
# # print(occup_gender.loc[: , 'gender'])
# print(occup_gender)

data=pd.read_excel(r"D:\users.xlsx",header=[1],index_col="行标签").iloc[:,1:] #配合EXCEL统计分组占比
# data.index=data["行标签"]
print(data.head(5))
