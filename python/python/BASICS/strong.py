inp=input("Enter a number:")                    
sum=0
if inp>0:
	for i in str(inp):
	    fact=1
    if (int(i)!=0):
             for j in range(1,int(i)+1):
                fact=fact*j                 
	sum=sum+fact
	if sum==inp:                            
	    print ("Given number is strong number")
	else:
	   print ("Given number is not strong number") 
    else:
	print ("Given number is not strong number" )
