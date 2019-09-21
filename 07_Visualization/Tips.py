#######模块导入
import pandas as pd
import numpy as np
import collections
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

###### 解决中文字体显示问题
font = {'family' : 'SimHei'}
plt.rc('font', **font)

#####数据准备
# tips=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv")
# tips.to_csv("tips",index=False)
tips=pd.read_csv("tips")
tips.drop("Unnamed: 0",axis=1,inplace=True)
print(tips.head())
# df=tips.groupby("day")["total_bill"].sum().sort_values(ascending=False)
sns.set(style="ticks") # 1.darkgrid（灰色网格 2.whitegrid（白色网格）  3.dark（黑色） 4.white（白色） 5.ticks（十字叉）


sns.distplot(tips.total_bill,bins=20,kde=False, rug=False,fit=stats.gamma,color="gray"); #kde：密度曲线；fit：拟合方式fit=stats.gamma

# sns.regplot(tip,size,data=tips)
# sns.relplot(x="total_bill", y="tip", data=tips)
#
# sns.relplot(x="total_bill", y="tip",hue="size", data=tips)
#
# sns.relplot(x="day", y="total_bill", data=tips)
sns.regplot(x="total_bill", y="tip",data=tips,fit_reg=stats.gamma)
sns.relplot(x="day", y="tip", hue="sex",data=tips,palette="deep")
sns.pairplot(tips) #多重变量比较

g = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True) #数据网格化
bins = np.linspace(0, 60, 13)
g.map(plt.hist, "total_bill", color="steelblue", bins=bins) #数据可视化


# get coeffs of linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(tips['total_bill'],tips['tip'])

# use line_kws to set line label for legend
ax = sns.regplot(x="total_bill", y="tip", data=tips, color='b',
 line_kws={'label':"y={0:.1f}x+{1:.1f}".format(slope,intercept)})

# plot legend
ax.legend()

plt.show()
