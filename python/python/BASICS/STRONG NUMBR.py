"""STRONG NUMBER
1!+4!+5! = 145"""
def strong():
    x=int(input("enter the number to be checked - "))
    
    z=x
    
    s=0
    while(x!=0):
        r=int (x%10)
        fact=1
        for i in range(1,r+1,1):
            fact=fact*i
            t=fact
        
            
            
        s=s+t
        x=x//10
    if(s==z):
        print("THE NUMBER ENTERED",z," IS STRONG NUMBER")
    else:
        print("THE NUMBER ENTERED",z," IS  NOT STRONG NUMBER")
        
strong()    
