def bill():
    print("APPLICATION TO PRINT CONSUMPTION OF ELECTRICITY")
    x=int(input("enter load in kilo-watt -  "))
    y=int(input("enter room no. -  "))
    c=int(input("enter units consumed in units/pm -  "))
    if(x<2):
        fix=40.0
        if(0<c<200):
            rate=3.70
        elif(201<c<400):
            rate=5.50
        else:
            rate=6.50
    elif(2<x<5):
        fix=100.0
        if(0<c<200):
            rate=3.70
        elif(201<c<400):
            rate=5.50
        else:
            rate=6.50
    else:
        fix= 20.0*x
        if(0<c<200):
            rate=3.70
        elif(201<c<400):
            rate=5.50
        else:
            rate=6.50
    charge=fix+rate
    
    print("\t \t BILL")
    print("*"*80)
    print("ROOM number - ",y)
    print("LOAD CONSUMED -  "  ,x,"KW")
    print("units CONSUMED - ",c, "UNITS/PM")
    print(" FIX CHARGES - ",fix," Rs")
    print("UNITS CONSUMED CHARGES - ",rate," Rs")
    print("AMOUNT PAYABLE BEFORE DUE DATE: ",charge ,"Rs")
    print("AMOUNT PAYABLE after DUE DATE: ", charge+100,"Rs")
    print("*"*80)
bill()
    
    
            
