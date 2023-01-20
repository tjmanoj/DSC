import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
d=pd.read_csv("diabetes_pima.csv")
x=d.iloc[:,5].values.reshape(-1,1)
y=d.iloc[:,8].values.reshape(-1,1)
plt.scatter(x,y)
plt.xlabel("BMI")
plt.ylabel("Outcome")
sns.regplot(x=x,y=y,data=d,logistic=True,ci=None)
plt.show()
