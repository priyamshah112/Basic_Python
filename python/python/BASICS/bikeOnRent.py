"""5.	Define a class called mobike with the following description: 					
Instance variables/data members:   
		int bno – to store the bike’s number
		int phno – to store the phone number of the customer
		String name – to store the name of the customer
		int days – to store the number of days the bike is taken on rent
		int charge – to calculate and store the rental charge
	Member methods:
		void input( ) – to input and store the detail of the customer.
		void computer( ) – to compute the rental charge
	The rent for a mobike is charged on the following basis.
		First five days 	Rs 500 per day;
		Next five days	Rs 400 per day
		Rest of the days 	Rs 200 per day

	void display ( ) – to display the details in the following format:

	Bike No. 	PhoneNo.	 No. of days Charge
"""
print("APPLICATION TO TAKE BIKE ON RENT")
def mobike():
    bno  = int(input(" Enter the bike's number - "))
    phno =int(input(" Enter the phone number - "))
    name = str(input("ENTER your name - "))
    
    days = int(input(" Enter the number of days - "))
    
        
    if(days<=5):
            charge = days*500
            
    elif(days>5 and days<10):
            a = days-5;
            charge = 5*500 + a*400;
            
    else:
            b = days - 10;
            charge = 5*500+5*400+b*200;
            
            
    
        


    print("bike number \t  phone number \t  name \t number of days \t rent ")
    print( bno , "\t  \t" , phno ,"\t \t" , name ,"\t \t" , days ,"\t \t" , charge );
    continue1()


def continue1():
    print("enter your choice to recheck for other number of days  press 1 to check press 0 to exit")
    chc=int(input("enter choice - "))
    if chc == 1:
        days();
    elif chc == 0:
        print("Thank You")
        return;
    else:
        print("Wrong Choice..! Try Again")
        continue1()

        
    
mobike();
        
    
