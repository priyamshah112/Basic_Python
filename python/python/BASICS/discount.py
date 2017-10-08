def dis():
    """
IT Gives Discount based on age ,gender and sales amount"""
    age=int(input("Enter your age "));
    s=int(input("Enter the sales amount "));
    g=str(input("Enter your gender(male or female or trans) "));
    a=0;
    d=0;
    if(age>=60):
        if(s<10000):

            if(g=='male'):
                
               d=0;
            elif(g=='female' or g=='trans' ):
            
               d=0.5;
            else:
                print("Wrong gender");
                return ;
                
            
                       
        elif(s>10000 and s<50000):
            if(g=='male'):
               
               d=0.10;
            elif(g=='female' or g=='trans' ):
            
              d=0.15;
            else:
                print("Wrong gender");
                return ;
              
              
        elif( s>50000):
            if(g=='male'):
               
               d=0.15;
            elif(g=='female' or g=='trans' ):
            
              d=0.20;
            else:
                print("Wrong gender");
                return ;
            
        
        
    else:
            d=0;

    a=s-(s*d);
    print("Amount Payable=",a);      

            
