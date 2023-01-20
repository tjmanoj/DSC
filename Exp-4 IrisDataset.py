import pandas as pd
d=pd.read_csv("E:\COLLEGE\DSC\Data Science Lab\iris.csv")
print("Top rows\n",d.head())                          #head() prints 1st 5 rows
n=int(input("Enter no.of samples to display:"))
print(d.sample(n))
print("Order of sheet:",d.shape,"\ncolumns are\n",d.columns)
n=input("Enter column name to display:")
print(d[n])
r=int(input("Enter row number to display:"))
print(d.iloc[r])
c1,c2=input("Enter column name and new name:").split()
d.rename(columns={c1:c2},inplace=True)
print("After replacement:\n",d)
st=int(input("Enter start value:"))
sp=int(input("Enter end value:"))
print("Sliced data:\n",d[st:sp+1])
n=input("Enter column name to calculate mean,median,sum,maximum and minimum:")
print("Mean\t:",d[n].mean(),"\n"
    "Median\t:",d[n].median(),"\n"
    "Mode\t:",d[n].mode(),"\n"
    "Sum\t:",d[n].sum(),"\n"
    "Maximum\t:",d[n].max(),"\n"
    "Minimum\t:",d[n].min())

