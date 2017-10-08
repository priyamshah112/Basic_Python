import math
def calArea():
    choice = int(input("Press 1 : To find area of Circle \nPress 2 : To find area of Square \nPress 3 : To find area of Rectangle \n"))
    

    if choice == 1:
        areaCircle();
    elif choice == 2:
        areaSquare();
    elif choice == 3:
        areaRectangle();
    else :
        print("Wrong Choice..! Try Again")
        calArea();

def areaCircle():
    print("\tYour Choice : To find area of circle\t")
    radius = int(input("Enter value for radius: "))
    areaCir = math.pi*radius*radius
    print("Area of Circle ==> ",areaCir)
    continue1()

def areaSquare():
    print("Your Choice : To find area of Square\n")
    side = int(input("Enter value for side : "))
    areaSq = side * side
    print("Area of Square ==> ",areaSq)
    continue1()

def areaRectangle():
    print("Your Choice : To find area of Rectangle\n")
    length = int(input("Enter value for lengrth: "))
    breadth = int(input("Enter value for breadth: "))
    print("Area of Rectangle ==> ",(length*breadth))
    continue1()

def continue1():
    chc = int(input("Press 1 to continue \n Press 0 to Exit \n"))
    if chc == 1:
        calArea()
    elif chc == 0:
        print("Thank You")
        return;
    else:
        print("Wrong Choice..! Try Again")
        continue1()

calArea();

