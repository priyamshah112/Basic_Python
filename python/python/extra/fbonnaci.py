def fibo():
    print("application to print fibo series")
    s = int(input("enter the number "))
    f =0
    f1 = 1
    k =0
    for i in range(0,s+1,1):
        k = f+f1
        f = f1
        f1 = k
    print(k)
        
fibo()
