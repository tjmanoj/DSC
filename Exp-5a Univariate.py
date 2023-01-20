import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew
import statistics as st
print("MENU\n1.UCI dataset 2.PIMA dataset 3.Exit")
ch=int(input("Enter choice:"))
while(ch!=3):
     if(ch==1):
        d=pd.read_csv("diabetes_uci.csv")
     elif(ch==2):
        d=pd.read_csv("diabetes_pima.csv")
     else:
         print("Invalid choice")
     print("Top rows:\n",d.head())
     print("Bottom rows:\n",d.tail())
     a=input("Enter column name:")
     print("Mean:",d[a].mean(),
           "\nMedian:",d[a].median(),
           "\nMode:",d[a].mode(),
           "\nFrequency:",d[a].value_counts(),
           "\nSkewness:",skew(d[a],axis=0,bias=True),
           "\nKurtosis:",kurtosis(d[a],axis=0,bias=True),
           "\nVaiance:",st.variance(d[a]),
           "\nStandard Deviation:",st.stdev(d[a]))               #round(st.stdev(d[a]),1))
     ch=int(input("Enter choice:"))
     
