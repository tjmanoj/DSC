import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
d=pd.read_csv("diabetes_pima.csv")
sns.set_style("white")
print(d.columns)
a=input("Enter column name:")
b=input("Enter another column name:")
sns.kdeplot(x=d[a],y=d[b])
plt.show()
sns.kdeplot(x=d[a],y=d[b],cmap="Reds",fill=True,bw_adjust=0.5)
plt.show()
sns.kdeplot(x=d[a],y=d[b],cmap="Blues",fill=True,thresh=0)
plt.show()
