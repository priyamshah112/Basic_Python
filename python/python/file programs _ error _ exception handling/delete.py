import os
def delete():
    
    x = input("enter employee id - ")
    if os.path.exists(x):
         os.remove(x)
         print("employee id",x,"is removed")
    else:
         print("sorry i cant delete %s file")
    
delete()
