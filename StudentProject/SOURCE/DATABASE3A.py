import sqlite3

def createTable():
    connection = sqlite3.connect('FYBTECH_A.db')

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
    connection.execute("CREATE TABLE BEEE(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO BEEE VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM BEEE")
    
    for data in result:
     
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])
    
###############################################################################################
    connection.execute("CREATE TABLE EG(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO EG VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM EG")
    
    for data in result:
       
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])
    
####################################################################################################3
    connection.execute("CREATE TABLE CS(STUDENT_ID INT,DIV TEXT,ATTENDANCE INT NOT NULL,UT INT,SEM INT,GRADE TEXT )")

    connection.execute("INSERT INTO CS VALUES(?,?,?,?,?,?)",('1000','A','100','30','70','AA'))

    connection.commit()

    result = connection.execute("SELECT * FROM CS")
    
    for data in result:
        print("STUDENT_ID: ",data[0])
        print("DIV:",data[1])
        print("ATTENDANCE:",data[2])
        print("UT:",data[3])
        print("SEM:",data[4])
        print("GRADE:",data[5])

    connection.close()
createTable()
        
