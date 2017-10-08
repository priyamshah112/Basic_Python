def zeroerr():
 try:
    x = int(input(" enter num.1 - "))
    y = int(input(" enter num.2 - "))
    sum = (x/y)
    print(sum)
 except (ZeroDivisionError) as e:
    #raise , e is exception object to call err and let program run while calling it
    print(e,"plese try again...!")
    zeroerr()
 except TypeError:
    print(" that was a string !")
    zeroerr()
 except ValueError:
    print("value error!")
    zeroerr()
"""except NameError:
     print("error name")
     zeroerr()
 except(ValueError,TypeError,ZeroDivisionError):
      print("OOPS! u gone wrong!")"""
    
zeroerr()
