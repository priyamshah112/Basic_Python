def file1():
    with open('priyam.txt' ,'r') as file:
        firstchar = file.read(30)
        restchar = file.read()
        content = file.read()
    print("the first chars are - ",firstchar)
    print("the rest chars are - ",restchar)
    file.close()
    
file1()
