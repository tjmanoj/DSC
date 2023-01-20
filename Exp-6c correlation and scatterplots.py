import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
d=pd.read_csv("diabetes_pima.csv")
print(d.columns)
x=input("Enter column name:")
y=input("Enter another column name:")
ax=sns.scatterplot(x=x,y=y,data=d)
plt.show()
cnormal=d.corr()
round=(cnormal,2)
sns.heatmap(cnormal)
plt.show()
