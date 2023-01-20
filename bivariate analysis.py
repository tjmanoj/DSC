import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from scipy import stats
logreg=LogisticRegression()
linreg=LinearRegression()
d=pd.read_csv("diabetes_uci.csv")
print(d.head())
x=d.iloc[:,5].values.reshape(-1,1)
y=d.iloc[:,1].values.reshape(-1,1)
linreg.fit(x,y)
plt.scatter(x,y)
plt.title("Linear Regression")
plt.xlabel("BMI")
plt.ylabel("Glucose")
plt.plot(x,linreg.predict(x),color="Blue")
plt.show()
print("Logistic regression")
x=d.iloc[:,5].values
y=d.iloc[:,4].values
plt.scatter(x,y)
x=d.iloc[:,5].values.reshape(-1,1)
y=d.iloc[:,8].values.reshape(-1,1)
def sig(x):
    t=np.exp(-x)
    return(1/1+t)
y_pred=sig(x)
logreg.fit(x,y)
plt.scatter(x,y)
plt.title("Diabetes logistic regression")
plt.xlabel("BMI")
plt.ylabel("Diabetes coefficient")
sns.regplot(x=x,y=y_pred,data=d,logistic=True,color="Red")
plt.show()
