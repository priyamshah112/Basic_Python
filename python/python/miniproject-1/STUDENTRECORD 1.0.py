"""PROGRAM TO KEEP TRACK RECORD OF  A ENGINEERING STUDENT's GRADES,ATTENDANCE,EXPOSURE COURSE,PROCTOR,EXTRA ACTIVITIES etc
                                   THE STUDENT RECORD(version 1)
The record has 5 choices 1]create record,2]read record,3]append reccord,4]delete record,5]exit.

1]Create record - Takes input as ROLL NUMBER,STUDENT NAME,PROCTOR NAME,EXPOSURE COURSE,OTHER ACTIVITIES,ATTENDANCE OF OVERALL SUBJECTS (IN %).
The file created is of file name-roll number.After taking basic information of a student the second input is of Grades .There is selection option 
between 9 first year engineering subjects out of which 6 can be selected.The basic information subject such as roll number,attendance in that particular 
subject and student test and sem marks are taken as input after an output is displayed which says whether the student is passed with distinction(<75%) 
or pass (32<total>75) or fail(32<).

2] READ RECORD -IT takes input of roll number and displays the related file content regarding that student if file not found it gives an error.

3] APPEND RECORD - The roll number is taken as input along with the editors name .The comment could be added regarding the change of marks,performance,etc.
if file is not found it creates a new file of that roll number.

4] Delete record - The roll number is taken as input and the file is deleted.if file not found error is given.

5] EXIT - The program is terminated and a Thank you! message is displayed.

*After every choice the choice program is called for further process."""
print(" \t \t ~ APPLICATION FOR STUDENT RECORD ~")
print("*"*80)
import os
def combo():
    print(" \t \t ~ Student Record ~ ")
    print(" 1] CREATE Student RECORD \n 2] READ Student RECORD \n 3] ADD DETAIL TO EXISTING RECORD \n 4] DELETE EXISTING Student Record \n 5] EXIT ")
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
    print(" \t \t ~ CREATE Student ID ~")
    x = (input("\t \t enter Student Roll number - "))
    y = (input("\t \t enter Student name - "))
    z = (input("\t \t enter Proctor name - "))
    
    p = (input("\t \t Student Exposure course - "))
    q = (input("\t \t Student Extra Activities - "))
    k=(input("\t \t ATTENDANCE (IN %) TILL DATE of all subjects - "))
    with open(x,'w') as t: 
        content = t.write( " ROLL NUMBER - %s \n STUDENT Name -%s \n PROCTOR NAME - %s \n EXPOSURE COURSE - %s \n OTHER ACTIVITY - %s \n ATTENDANCE(in percentage) - %s \n "  % (x,y,z,p,q,k))
    
    
    
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of PHYSICS - "))
           w=int(input("enter test marks of physics out of 30 -  "))
           e=int(input("enter sem marks of physics out of 70 -  "))
           
           calc = (w + e)
           
           
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of CHEMISTRY - "))
           w=int(input("enter test marks of chemistry out of 30 -  "))
           e=int(input("enter sem marks of chemistry out of 70 -  "))
           calc = (w + e)
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of MATHS - "))
           w=int(input("enter test marks of maths out of 40 -  "))
           e=int(input("enter sem marks of maths out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of CS - "))
           w=int(input("enter test marks of cs out of 30 -  "))
           e=int(input("enter sem marks of cs out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of EVS - "))
           w=int(input("enter test marks of evs out of 30 -  "))
           e=int(input("enter sem marks of evs out of 70 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of EG - "))
           w=int(input("enter test marks of eg out of 40 -  "))
           e=int(input("enter sem marks of eg out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of BEEE - "))
           w=int(input("enter test marks of beee out of 40 -  "))
           e=int(input("enter sem marks of beee out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of MECH - "))
           w=int(input("enter test marks of mech out of 40 -  "))
           e=int(input("enter sem marks of mech out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(x,'a') as t:
               
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
           x = (input("enter Student Roll number - "))
           k=(input("ATTENDANCE (IN %) TILL DATE of FCP - "))
           w=int(input("enter test marks of mech out of 40 -  "))
           e=int(input("enter sem marks of mech out of 60 -  "))
           calc = (w + e)
           print(calc , " out of 100")
           with open(x,'a') as t:
               
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
    x = input("enter STUDENT ROLL no. - ")
  
    with open(x,'r') as p:
               content = p.read()
    print(content)
    
    combo()

def insertrecord():
    
    print(" EDIT STUDENT ROLL no. ")
    x = (input("enter  roll number - "))
    
    y = (input("enter your name  - "))
    k = (input("comment - "))
    #fileName  = x+".txt"
    with open(x,'a') as t:
            content = t.write( "comment -  %s \n"  % (k))
    print(" student record ",x ," is edited  by ",y)
         
   
    combo()
import os
def delete():
    
    x = input("enter roll no.- ")
    if os.path.exists(x):
         os.remove(x)
         print("student record",x,"is removed")
    else:
         print("sorry i cant delete %s file")
    combo()
def exit():
    print("THANK YOU!")
combo()



