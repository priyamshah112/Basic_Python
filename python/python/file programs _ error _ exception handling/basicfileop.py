def file1():
    file = open('priyam.txt' ,'r')
    content = file.read()
    print(content)
    file.close()
    
file1()
