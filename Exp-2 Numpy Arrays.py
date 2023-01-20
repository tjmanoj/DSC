import numpy as np
l=[]
n=int(input("Enter no.of elements:"))
for i in range(n):
    element=int(input(f'Enter element{i+1}:'))
    l.append(element)
a=np.array(l)
print(a)
print("MENU\n1.Insert 2.Search 3.Delete 4.Sort 5.Exit")
ch=0
while(ch!=5):
    ch=int(input("Enter choice:"))
    if ch==1:
        b=int(input("Enter element to insert:"))
        c=int(input("Enter position:"))
        a=np.insert(a,c-1,b)
        print(a)
    elif ch==2:
        s=int(input("Enter a number:"))
        f=np.where(a==s)
        print(f) 
    elif ch==3:
        d=int(input("Enter index to remove:"))
        a=np.delete(a,d)
        print("Elements after deletion:",a)
    elif ch==4:
        print(np.sort(a))
    elif ch==5:
        print("End")
    else:
        print("Invalid choice:")
