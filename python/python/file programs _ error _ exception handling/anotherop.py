def file1():
    with open('priyam.txt' ,'r') as file:
        content = file.read()
    print(content)
    file.close()
    
file1()
