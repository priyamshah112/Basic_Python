"""PROGRAM TO KEEP TRACK RECORD OF  A ENGINEERING STUDENT's GRADES,ATTENDANCE,EXPOSURE COURSE,PROCTOR,EXTRA ACTIVITIES etc"""
print(" \t \t ~ APPLICATION FOR ENGINEERING STUDENT RECORD ~")
print("*"*80)

def combo():
    print(" \t \t ~ ENGINEERING Student Record ~ ")
    print(" 1] CREATE Student RECORD \n 2] READ Student RECORD \n 3] ADD DETAIL TO EXISTING RECORD \n 4] DELETE EXISTING Student Record \n 5] EXIT ")
    while True:
        try:
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
            del x
            
        except ValueError as e:
            print(e,"a wrong choice!")
            del x
            combo()

        
    
        

    combo()
import os 
def record():
    
      print(" \t \t ~ CREATE Student ID ~")
      r =input("\t \t enter Student Roll number - ")
      if (len(r)>3):
          print("please enter a valid roll number - ")
          record()
         
         
   
      if os.path.exists(r):
               print("already created ! if wanna update press 3")
      else:
               
               y = input("\t \t enter Student name - ")
           
            
               z = input("\t \t enter Proctor name - ")
           
               
            
               p =input("\t \t Student Exposure course - ")
           
               
            
               q = input("\t \t Student Extra Activities - ")
           
               
               k= input("\t \t ATTENDANCE (IN %) TILL DATE of all subjects - ")
             
               

    
               with open(r,'w') as t:
                    content = t.write( " ROLL NUMBER - %s \n STUDENT Name -%s \n PROCTOR NAME - %s \n EXPOSURE COURSE - %s \n OTHER ACTIVITY - %s \n ATTENDANCE(in percentage) - %s \n "  % (r,y,z,p,q,k))
               print(" \t SUBJECT \n select 6 subjects from the options \n 1] PHYSICS \n 2] CHEMISTRY \n 3] MATHS \n 4] COMMUNICATION SKILLS \n 5] EVS \n 6] MECHANCS \n 7] FCP \n 8] EG \n 9] BEEE")
               for i in range(1,7):
                        try:
        
                            t = int(input(" ENTER YOUR CHOICE - "))
                            if (t==1):
                                physics()
            
        
                            elif(t==2):
                                chemistry()
                            elif(t==3):
                                maths()
                            elif(t==4):
                                cs()
                            elif(t==5):
                                evs()
                            elif(t==6):
                                mech()
                            elif(t==7):
                                fcp()
                            elif(t==8):
                                eg()
                            elif(t==9):
                                beee()
                            else:
                                print("wrong choice! of subject number")
                                del t
                        except ValueError:
                                print("The entered value is not a valid number")
                                del t
                                
                                

        
           
def physics():
           print(" \t \t ~PHYSICS~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of PHYSICS - "))
           w=int(input("enter test marks of physics out of 30 -  "))
           e=int(input("enter sem marks of physics out of 70 -  "))
           
           calc = (w + e)
           
           
           with open(r,'a') as t:
               
               content=t.write(" \t \t ~ PHYSICS ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n  ATTENDANCE(in percentage) - %s   \n" % (w,e,calc,k))
           print(content)
           print(calc , " out of 100")
           if(calc>=75):
                 print("passed with distinction !")
           elif(75>calc>32):
                 print("pass !")
        
           else:
                 print("fail ")

def chemistry():
           print(" \t  \t ~ CHEMISTRY ~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of CHEMISTRY - "))
           w=int(input("enter test marks of chemistry out of 30 -  "))
           e=int(input("enter sem marks of chemistry out of 70 -  "))
           calc = (w + e)
           with open(r,'a') as t:
               
               content=t.write(" \t \t ~ CHEMISTRY ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n  ATTENDANCE(in percentage) - %s   \n" % (w,e,calc,k))
           print(content)
           print(calc , " out of 100")
           if(calc>=75):
               print("passed with distinction")
           elif(75>calc>32):
               print("pass")
        
           else:
                print("fail")
def maths():
           print(" \t \t ~ MATHS ~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of MATHS - "))
           w=int(input("enter test marks of maths out of 40 -  "))
           e=int(input("enter sem marks of maths out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(r,'a') as t:
               
               content=t.write(" \t \t ~ MATHS ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n ATTENDANCE(in percentage) - %s   \n" % (w,e,calc,k))
           print(content)
           if(calc>=75):
               print("passed with distinction !")
           elif(75>calc>32):
               print("pass !")
        
           else:
                print("fail")
def cs():
           print(" \t \t ~ COMMUNICATION SKILLS ~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of CS - "))
           w=int(input("enter test marks of cs out of 30 -  "))
           e=int(input("enter sem marks of cs out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(r,'a') as t:
               
               content=t.write(" \t \t ~ CS ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n ATTENDANCE(in percentage) - %s   \n" % (w,e,calc,k))
           print(content)
           if(calc>=75):
               print("passed with distinction !")
           elif(75>calc>32):
               print("pass !")
        
           else:
                print("fail")
def evs():
           print(" \t \t ~ EVS ~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of EVS - "))
           w=int(input("enter test marks of evs out of 30 -  "))
           e=int(input("enter sem marks of evs out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(r,'a') as t:
               
               content=t.write(" \t \t ~ EVS ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n ATTENDANCE(in percentage) - %s   \n" % (w,e,calc,k))
           print(content)
           if(calc>=75):
               print("passed with distinction !")
           elif(75>calc>32):
               print("pass !")
        
           else:
                print("fail")
def eg():
           print(" \t \t ~ ENGINEERING DRAWING ~  \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of EG - "))
           w=int(input("enter test marks of eg out of 40 -  "))
           e=int(input("enter sem marks of eg out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(r,'a') as t:
               
               content=t.write(" \t \t ~ EG ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n ATTENDANCE(in percentage) - %s   \n " % (w,e,calc,k))
           print(content)
           if(calc>=75):
               print("passed with distinction")
           elif(75>calc>32):
               print("pass")
        
           else:
                print("fail")
def beee():
           print(" \t \t ~ BEEE ~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of BEEE - "))
           w=int(input("enter test marks of beee out of 40 -  "))
           e=int(input("enter sem marks of beee out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(r,'a') as t:
               
               content=t.write("\t \t  ~ BEEE ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n ATTENDANCE(in percentage) - %s   \n" % (w,e,calc,k))
           print(content)
           if(calc>=75):
               print("passed with distinction")
           elif(75>calc>32):
               print("pass")
        
           else:
                print("fail")
def mech():
           print(" \t \t ~ MECHANICS ~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of MECH - "))
           w=int(input("enter test marks of mech out of 40 -  "))
           e=int(input("enter sem marks of mech out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(r,'a') as t:
               
               content=t.write(" \t \t ~ MECHANICS ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n ATTENDANCE(in percentage)- %s   \n" % (w,e,calc,k))
           print(content)
           if(calc>=75):
               print("passed with distinction")
           elif(75>calc>32):
               
               print("pass")
        
           else:
                print("fail")
def fcp():
           print(" \t \t ~ STRUCTURED PROGRAMMING ~ \n")
           r = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of FCP - "))
           w=int(input("enter test marks of mech out of 40 -  "))
           e=int(input("enter sem marks of mech out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(r,'a') as t:
               
               content=t.write("\t \t ~ FCP ~  \n TEST MARKS - %s  \n SEMSTER MARKS - %s  \n TOTAL SCORE -%s   \n ATTENDANCE(in percentage) - %s   \n" % (w,e,calc,k))
           print(content)
           if(calc>=75):
               print("passed with distinction")
           elif(75>calc>32):
               
               print("pass")
        
           else:
                print("fail")

           combo()

def readrecord():
   
    r = input("enter STUDENT ROLL no. - ")
     
  
    with open(r,'r') as p:
               content = p.read()
    print(content)
    
combo()

def insertrecord():
    
    print(" EDIT STUDENT ROLL no. ")
    r = input("enter  roll number - ")
    
    y = input("enter your name  - ")
    k = input("comment - ")
    #fileName  = x+".txt"
    with open(r,'a') as t:
        content = t.write( "comment -  %s \n"  % (k))
    print(" student record ",r," is edited  by ",y)
         
   
combo()
import os
def delete():
    
    r = input("enter roll no.- ")
    if os.path.exists(r):
         os.remove(r)
         print("student record",r,"is removed")
    else:
         print("sorry i cant delete %s file")
combo()
def exit():
    print("THANK YOU!")
    return
combo()



