import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
print("MENU\n1.UCI dataset 2.Pima dataset 3.Exit")
ch=int(input("Enter choice:"))
while(ch!=3):
     if(ch==1):
       d=pd.read_csv("diabetes_uci.csv")
     elif(ch==2):
       d=pd.read_csv("diabetes_pima.csv")
     else:
       print("Invalid choice")
     x=d.iloc[:,5].values.reshape(-1,1)
     y=d.iloc[:,1].values.reshape(-1,1)
     fig=plt.figure()
     ax=fig.add_subplot(projection='3d')
     ax.scatter(xs=x,ys=y)
     plt.show()
     ch=int(input("Enter choice:"))
