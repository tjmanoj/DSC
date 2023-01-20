import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
d=pd.read_csv("diabetes_pima.csv")
x=d.iloc[:,5].values.reshape(-1,1)
y=d.iloc[:,8].values.reshape(-1,1)    
plt.scatter(x,y)
plt.ylabel("BMI")
plt.xlabel("Outcome")
lin=LinearRegression()
lin.fit(x,y)
y_pred=lin.predict(x)
plt.plot(x,y_pred,color='Red')
plt.show()
