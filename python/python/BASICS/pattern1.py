def pattern1():
    n = int(input("enter number of rows to be print = "))
    for i in range(n+1):
        print(end= ' ')
        
        for j in range(1,i+1,1):
            print(j,end=' ')
        print("\n")  
pattern1()
