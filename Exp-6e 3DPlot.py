import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
d=pd.read_csv("iris.csv")
x=d.iloc[:,0].values.reshape(-1,1)
y=d.iloc[:,1].values.reshape(-1,1)
z=d.iloc[:,2].values.reshape(-1,1)
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
ax.set_zlabel('petal_length')
plt.show()
