#5.	Write a program to print name of student, marks of 5 subjects, total marks of all subjects and average marks .
def result():
     name_of_student=str(input("enter your name:"))
     p =int(input("enter your p marks out of 100:"))
     c =int(input("enter your c marks out of 100:"))
     m =int(input("enter your m marks out of 100:"))
     b =int(input("enter your b marks out of 100:"))
     cs =int(input("enter your cs marks out of 100:"))
     totalmarks=(p+c+m+b+cs)
     print("totalmarks="+str(totalmarks))
     average=(p+c+m+b+cs)/500
     print("average="+str(average))
    
     
     
