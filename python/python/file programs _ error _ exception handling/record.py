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
    t.close()
record()
