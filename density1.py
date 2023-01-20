import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
d=pd.read_csv("diabetes_pima.csv")
print(d.columns)
a=input("Enter column name:")
d[a].plot.density(color='blue')
plt.title('Density plot')
plt.xlabel(a)
plt.show()

a=input("Enter column name for x-axis:")
b=input("Enter column name for y-axis:")
x1=np.linspace(d[a].min(),d[a].max(),50)
y1=np.linspace(d[b].min(),d[b].max(),50)
x,y=np.meshgrid(x1,y1)
z=np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
plt.xlabel(a)
plt.ylabel(b)
plt.title('Contour Plot')
plt.contour(x,y,z)
plt.show()
