import sqlite3

def createTable():
    connection = sqlite3.connect('login1.db')

    connection.execute("CREATE TABLE USERS(STUDENT_LOGIN_ID TEXT NOT NULL,STUDENT_ID TEXT,FIRST_NAME TEXT,LAST_NAME TEXT,EMAIL TEXT,CONTACT_NUM TEXT,ADDRESS1 TEXT,ADDRESS2 TEXT,PIN TEXT,COURSECODE TEXT)")

    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)",('1000','1','PRIYAM','SHAH','PRIYAMSHAH112@GMAIL.COM','7738478888','A/50 XYZ DARSHAN','MHB COLONY ,JOG','400071','A'))

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")
    
    for data in result:
        print("STUDENT_LOGIN_ID : ",data[0])
        print("STUDENT_ID  :",data[1])
        print("FIRST_NAME :",data[2])
        print("LAST_NAME: ",data[3])
       # print("D.O.B: ",data[4])
    #    print("GENDER:",data[5])
        print("EMAIL :",data[4])
        print("CONTACT: ",data[5])
        print("ADDRESS1: ",data[6])
        print("ADDRESS2:",data[7])
        print("PIN :",data[8])
        print("COURSECODE : ",data[9])

    connection.close()

createTable()
        
    
#STUDENT_LOGIN_ID ,STUDENT_ID ,FIRST_NAME ,LAST_NAME ,D.O.B ,GENDER ,EMAIL ,CONTACT_NUM ,ADDRESS1,ADDRESS2 ,PIN ,COURSECODE
