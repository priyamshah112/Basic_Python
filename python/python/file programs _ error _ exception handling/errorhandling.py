import os 
def record():
    
      print(" \t \t ~ CREATE Student ID ~")
      x =int(input("\t \t enter Student Roll number - "))
      
      if(x>999):
         print("invalid roll no.")
         del x
        
         
   
      if os.path.exists(x):
               print("already created ! if wanna update press 3")
      else:
               x =int(input("\t \t enter Student Roll number - "))
               
               y = str(input("\t \t enter Student name - "))
           
            
               z = str(input("\t \t enter Proctor name - "))
           
               
            
               p = str(input("\t \t Student Exposure course - "))
           
               
            
               q = str(input("\t \t Student Extra Activities - "))
           
               
               k= int(input("\t \t ATTENDANCE (IN %) TILL DATE of all subjects - "))

               
               with open(x,'w') as t:
                  content = t.write( " ROLL NUMBER - %s \n STUDENT Name -%s \n PROCTOR NAME - %s \n EXPOSURE COURSE - %s \n OTHER ACTIVITY - %s \n ATTENDANCE(in percentage) - %s \n "  % (x,y,z,p,q,k))
record()
