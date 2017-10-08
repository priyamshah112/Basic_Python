print("APPLICATION FOR EMPLOYEE RECORD ")
print("*"*80)
def combo():
    print(" \t \t~ employee record ~")
    print("1] CREATE EMPLOYEE RECORD \n  2] READ EMPLOYEE RECORD \n  3] ADD DETAIL TO EXISTING RECORD \n 4]DELETE EXISTING FILE  \n 5] EXIT ")
    x = int(input(" ENTER YOUR CHOICE - "))
    if (x==1):
        record()
    elif(x==2):
        readrecord()
    elif(x==3):
        insertrecord()
    elif(x==4):
        delete()
    elif(x==5):
        exit()
    else:
        print("wrong choice! ")
        combo()
def record():
    print(" CREATE EMPLOYEE ID ")
    x = (input("enter your id number - "))
    y = (input("enter your name - "))
    z = (input("designation - "))
    k = (input("salary - "))
    #fileName  = x+".txt"
    with open(x,'w') as t:
        content = t.write( " id - %s \n  name -%s \n designation - %s \n salary - %s \n"  % (x,y,z,k))
    print(" employe ",x ," is created ")
    combo()
def readrecord():
    x = input("enter employee id no. - ")
    with open(x,'r') as p:
        content = p.read()
    print(content)
    combo()
def insertrecord():
    print(" EDIT EMPLOYEE ID ")
    x = (input("enter your id number - "))
    k = (input("extra comment - "))
    #fileName  = x+".txt"
    with open(x,'a') as t:
        content = t.write( " extra comment %s \n"  % (k))
    print(" employee ",x ," is edited ")
    combo()
import os
def delete():
    
    x = input("enter employee id - ")
    if os.path.exists(x):
         os.remove(x)
         print("employee id",x,"is removed")
    else:
         print("sorry i cant delete %s file")
    combo()
def exit():
    print("THANK YOU!")
combo()



