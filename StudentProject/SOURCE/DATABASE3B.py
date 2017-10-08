import sqlite3

def createTable():
    connection = sqlite3.connect('FYBTECH_B.db')

    connection.execute("CREATE TABLE PHYSICS(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO PHYSICS VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM PHYSICS")
    
    for data in result:
     
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])
    
##########################################################################
    connection.execute("CREATE TABLE MATHS(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO MATHS VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM MATHS")
    
    for data in result:
   
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])
    
##################################################################
    connection.execute("CREATE TABLE CHEMISTRY(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO CHEMISTRY VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM CHEMISTRY")
    
    for data in result:
    
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])
    
#########################################################################################
    connection.execute("CREATE TABLE FCP(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO FCP VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM FCP")
    
    for data in result:
     
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])
    
###############################################################################################
    connection.execute("CREATE TABLE MECH(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO MECH VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM MECH")
    
    for data in result:
       
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])
    
####################################################################################################3
    connection.execute("CREATE TABLE EVS(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO EVS VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM EVS")
    
    for data in result:
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])

    connection.close()
createTable()
        
