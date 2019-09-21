import pandas as pd
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
regiment=pd.DataFrame(raw_data)
# print(regiment.head())
# print(regiment[regiment["regiment"]=='Nighthawks']["preTestScore"].mean())
# print(regiment["company"].describe())
# print(regiment.groupby("company")["preTestScore"].mean()) #分层索引
# print(regiment.groupby(["regiment","company"])["preTestScore"].mean().unstack()) #非分层索引的形式
# print(regiment.groupby(["regiment","company"]).mean())
# print(regiment.groupby(["regiment","company"]).size())
for name,group in regiment.groupby("regiment"):  #打印DataFrameGroupBy各属性
    print(name)
    print(group)
