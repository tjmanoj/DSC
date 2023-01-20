import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
d= pd.read_csv("diabetes_pima.csv")
print(d.columns)
a=input("Enter column name:")
sns.histplot(d[a])
plt.show()
