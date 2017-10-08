"""PROGRAM TO KEEP TRACK RECORD OF  A ENGINEERING STUDENT's GRADES,ATTENDANCE,EXPOSURE COURSE,PROCTOR,EXTRA ACTIVITIES etc"""
print(" \t \t ~ APPLICATION FOR STUDENT RECORD ")
print("*"*80)
def combo():
    print(" \t \t ~ Student Record ~ ")
    print("1] CREATE Student RECORD \n 2] READ Student RECORD \n 3] ADD DETAIL TO EXISTING RECORD \n 4] DELETE EXISTING Student Record \n 5] EXIT ")
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
        combo()
def record():
    print(" \t \t ~ CREATE Student ID ")
    x = (input("enter Student Roll number - "))
    y = (input("enter Student name - "))
    z = (input("enter Proctor name - "))
    
    p = (input("Student Exposure course - "))
    q = (input("Student Extra Activities - "))
    k=(input("ATTENDANCE (IN %) TILL DATE of all subjects - "))
    with open(x,'w') as t: 
        content = t.write( "ROLL NUMBER - %s \n  STUDENT name -%s \n PROCTOR NAME - %s \n EXPOSURE COURSE - %s \n OTHER ACTIVITY - %s \n ATTENDANCE - %s \n "  % (x,y,z,p,q,k))
    print(" STUDENT RECORD ",x ," is created ")
    
    
    print(" \t SUBJECT \n select 6 subjects from the options \n 1] PHYSICS \n 2] CHEMISTRY \n 3] MATHS \n 4] COMMUNICATION SKILLS \n 5] EVS \n 6] MECHANCS \n 7] FCP \n 8] EG \n 9] BEEE")
    for i in range(1,7):
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
           print("wrong choice! ")

        
           
def physics():
           print(" \t \t ~PHYSICS~ \n")
           w=int(input("enter test marks of physics out of 30 -  "))
           e=int(input("enter sem marks of physics out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           content=t.write(" ~ PHYSICS ~ \n TEST MARKS -  \n SEMSTER MARKS - \n TOTAL SCORE - \n " % (w,e,calc))
           print(content)
           if(calc>75):
                 print("passed with distinction !")
           elif(75>calc>32):
                 print("pass !")
        
           else:
                 print("fail ")

def chemistry():
           print(" \t \t ~ CHEMISTRY ~ \n")
           w=int(input("enter test marks of chemistry out of 30 -  "))
           e=int(input("enter sem marks of chemistry out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           if(calc>75):
               print("passed with distinction")
           elif(75>calc>32):
               print("pass")
        
           else:
                print("fail")
def maths():
           print(" \t \t ~ MATHS ~ \n")
           w=int(input("enter test marks of maths out of 40 -  "))
           e=int(input("enter sem marks of maths out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           if(calc>75):
               print("passed with distinction !")
           elif(75>calc>32):
               print("pass !")
        
           else:
                print("fail")
def cs():
           print(" \t \t ~ COMMUNICATION SKILLS ~ \n")
           w=int(input("enter test marks of cs out of 30 -  "))
           e=int(input("enter sem marks of cs out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           if(calc>75):
               print("passed with distinction !")
           elif(75>calc>32):
               print("pass !")
        
           else:
                print("fail")
def evs():
           print(" \t \t ~ EVS ~ \n")
           w=int(input("enter test marks of evs out of 30 -  "))
           e=int(input("enter sem marks of evs out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           if(calc>75):
               print("passed with distinction !")
           elif(75>calc>32):
               print("pass !")
        
           else:
                print("fail")
def eg():
           print(" \t \t ~ ENGINEERING DRAWING ~  \n")
           w=int(input("enter test marks of eg out of 40 -  "))
           e=int(input("enter sem marks of eg out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           if(calc>75):
               print("passed with distinction")
           elif(75>calc>32):
               print("pass")
        
           else:
                print("fail")
def beee():
           print(" \t \t ~ BEEE ~ \n")
           w=int(input("enter test marks of beee out of 40 -  "))
           e=int(input("enter sem marks of beee out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           if(calc>75):
               print("passed with distinction")
           elif(75>calc>32):
               print("pass")
        
           else:
                print("fail")
def mech():
           print(" \t \t ~ MECHANICS ~ \n")
           w=int(input("enter test marks of mech out of 40 -  "))
           e=int(input("enter sem marks of mech out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           if(calc>75):
               print("passed with distinction")
           elif(75>calc>32):
               
               print("pass")
        
           else:
                print("fail")
           
        
    #fileName  = x+".txt"
    
    
combo()
def readrecord():
    x = input("enter STUDENT ROLL no. - ")
    with open(x,'r') as p:
        content = p.read()
    print(content)
    combo()
def insertrecord():
    print(" EDIT STUDENT ROLL no. ")
    x = (input("enter your roll number - "))
    k = (input("comment - "))
    #fileName  = x+".txt"
    with open(x,'a') as t:
        content = t.write( "comment -  %s \n"  % (k))
    print(" employee ",x ," is edited ")
    combo()
import os
def delete():
    
    x = input("enter roll no.- ")
    if os.path.exists(x):
         os.remove(x)
         print("employee id",x,"is removed")
    else:
         print("sorry i cant delete %s file")
    combo()
def exit():
    print("THANK YOU!")
combo()



