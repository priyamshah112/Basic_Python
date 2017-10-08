def demorun():
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
           if(calc>75):
                 print("passed with distinction !")
           elif(75>calc>32):
                 print("pass !")
        
           else:
                 print("fail ")

def chemistry():
           print(" \t \t ~ CHEMISTRY \n")
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
           print(" \t \t ~ MATHS \n")
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
           print(" \t \t ~ COMMUNICATION SKILLS \n")
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
           print(" \t \t ~ EVS \n")
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
           print(" \t \t ~ ENGINEERING DRAWING \n")
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
           print(" \t \t ~ BEEE\n")
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
           print(" \t \t ~ MECHANICS \n")
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
demorun()
