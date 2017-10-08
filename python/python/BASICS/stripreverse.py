def file1():
    with open('priyam.txt' ,'r') as file:
       p = file.readline()
       print(p)
    for q in reversed(p):
       print(q.strip())

    
file1()
