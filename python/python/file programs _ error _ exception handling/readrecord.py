def readrecord():
    x = input("enter employee id no. - ")
    with open(x,'r') as p:
        content = p.read()
    print(content)
readrecord()
        
