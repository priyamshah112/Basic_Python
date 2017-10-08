def tax():
    print("PROGRAM TO CALCULATE INCOME TAX")
    sal=float(input("enter your salary = "))
    name=str(input("enter your name = "))
    if(sal > 69000):
        tx=20.0
    elif(47500 <sal>68999):
        tx=15.0
    else:
        tx=10.0
    amt=(sal*tx)/100.0
    print("\t \t INVOICE \t \t")
    print("*"*80)
    print("name - ",name)
    print("monthly salary - ",sal)
    print("tax - %",tx)
    print("tax amount payable - ",amt)
    
    print("*"*80)
tax()
