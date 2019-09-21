import pandas as pd
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}
army=pd.DataFrame(raw_data)
# pd.set_option('display.max_columns', None) #显示所有列
army.index=army["origin"]
# print(army.head())
# print(army["veterans"])
# print(army[["veterans","deaths"]]) #只取"veterans","deaths"两列，也可以使用df.loc[]方法
# print(army.columns)
# print(army[army["origin"].isin(["Maine","Alaska"])][["deaths","size","deserters"]])
# print(army.loc[["Maine","Alaska"],["deaths","size","deserters"]])
# print(army.iloc[3:7,3:6])
# print(army.iloc[5:,])
# print(army.iloc[:,3:8])
# print(army[(army["deaths"]>500)|(army["deaths"]<50)])
# print(army[army["regiment"]!="Dragoons"])
# print(army[army["origin"].isin(["Texas","Arizona"])])
# print(army[army["origin"].isin(["Arizona"])].iloc[:,3])
print(army.iloc[2,army.columns.get_loc("deaths")]) #解决混合索引问题
