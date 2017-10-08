def u():
    
 try:
    x = int(input(" enter num.1 - "))
    y = int(input(" enter num.2 - "))
    sum = (x/y)
    print(sum)
 except (ZeroDivisionError) as e:
    #raise , e is exception object to call err and let program run while calling it
    print(e,"plese try again...!")
    u()
 except TypeError:
    print(" that was a string !")
    u()
 except ValueError:
    print("value error!")
    u()
 else:
     print("good")
 finally:
     print("chava run re")
     
     del x
     del y
     
u()
