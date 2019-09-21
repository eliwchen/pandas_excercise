#######模块导入
import pandas as pd
import collections
import matplotlib.pyplot as plt

###### 解决中文字体显示问题
font = {'family' : 'SimHei'}
plt.rc('font', **font)

#####数据准备
# titanic=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv")
# titanic.to_csv("titanic",index=False)
titanic=pd.read_csv("titanic")
print(titanic.head())
titanic.set_index('PassengerId').head()
# sum the instances of males and females
males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()

# put them into a list called proportions
proportions = [males, females]

# Create a pie chart
plt.pie(
    # using proportions
    proportions,
    # with the labels being officer names
    labels=['Males', 'Females'],
    # with no shadows
    shadow=False,
    # with colors
    colors=['blue', 'red'],
    # with one slide exploded out
    explode=(0.15, 0),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%'
)

# View the plot drop above
plt.axis('equal')
# Set labels
plt.title("Sex Proportion")

# View the plot
plt.tight_layout()
plt.show()
# creates the plot using
lm = sns.lmplot(x = 'Age', y = 'Fare', data = titanic, hue = 'Sex', fit_reg=False)

# set title
lm.set(title = 'Fare x Age')

# get the axes object and tweak it
axes = lm.axes
axes[0,0].set_ylim(-5,)
axes[0,0].set_xlim(-5,85)
titanic.Survived.sum()

# sort the values from the top to the least value and slice the first 5 items
df = titanic.Fare.sort_values(ascending = False)
print(df)

# create bins interval using numpy
binsVal = np.arange(0,600,10)
print(binsVal)

# create the plot
plt.hist(df, bins = binsVal)

# Set the title and labels
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')
# show the plot
plt.show()
