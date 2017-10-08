print(" THE DICE GAME")
pl = str(input("enter your name player 1 - "))
p2 = str(input("enter your name player 2 - "))
def dice():
    
    x =[1,2,3,4,5,6]
    count=0
    count1 = 0
    for i in range(0,20,1):
        t1 = int(input("enter the dice result p1- "))
        if (0 > t1 > 6):
            print("invalid result pls put a valid choice ")
            continue1();
        t2 = int(input("enter the dice result p2 - "))
        if (0 > t2 > 6):
            print("invalid result pls put a valid choice ")
            continue1();
        count = count + t1
        count1 = count1 + t2 
    if(count <= 20):
         print("cool you won the game ",p1)
    
       
    elif(count1 <= 20):
         print("cool you won the game ",p2)
    else:
        print("game is draw")
def continue1():
    print("print your choice press 1 to continue or press 0 to leave")
    chc = int(input("enter choice - "))
    if(chc == 1):
         dice();
    elif(chc==0):
        print("thank you")
    else:
        print("invalid choice")
dice()
        
        
        
        
