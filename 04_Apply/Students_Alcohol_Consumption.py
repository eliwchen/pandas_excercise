import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv")
# print(df.head())
# print(df.info())
# print(df.columns)
# print(df.loc[:,"school":"guardian"])
capitalizer=lambda x: x.str.capitalize() #创建一个lambda函数用于将字符串首字母大写
print(df[["Mjob","Fjob"]].apply(capitalizer)) #Pandas 文本数据方法 capitalize( ) lower( ) upper( )
#map(str.upper),map(str.lower),map(str.title)  series级别的转换操作
# print(df.iloc[-1,-1])

# def majority(num):  #调用series中的数值
#     if num> 17:
#         return True
#     else:
#         return False
# df['legal_drinker']=df["age"].apply(majority)
# print(df)

# df['legal_drinker'] = df['age'].apply(lambda x:1 if x>17 else(0)) #采用lambda函数法
# print(df)
# def time10(x):
#     if type(x) is int:
#         return x*10
#     else:
#         return x
time10=lambda x:x*10 if (type(x) is int) else(x)
print(df.applymap(time10))
