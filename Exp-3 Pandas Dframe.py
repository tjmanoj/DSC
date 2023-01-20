import pandas as pd
name,roll,m1,m2,m3,m4,result=([]for i in range(7))
n=int(input("Enter number of students:"))
for i in range(n):
    a=str(input("Enter student name:\t"))
    name.append(a)
    b=str(input("Enter roll number:\t"))
    roll.append(b)
    c=int(input("Enter Tamil mark:\t"))
    m1.append(c)
    d=int(input("Enter English mark:\t"))
    m2.append(d)
    e=int(input("Enter Maths mark:\t"))
    m3.append(e)
    f=int(input("Enter Social mark:\t"))
    m4.append(f)
    if c<=35 or d<=35 or e<=35 or f<=35:
        result.append("Fail")
    else:
        result.append("Pass")
final=list(zip(name,roll,m1,m2,m3,m4,result))
data=pd.DataFrame(final,columns=["Name","Roll.no","Tamil","English","Maths","Social","Result"])
print(data)

