def file1():
    with open('priyam.txt','r') as p:
        for line in p:
            print(len(line))
file1()
