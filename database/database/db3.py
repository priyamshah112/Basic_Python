import sqlite3 as a
import sys #system
x=int(input("enter car id - "))
y=str(input("enter car name "))
z=int(input("car rate -  "))
con = a.connect('cars.db')
with  con:
   cur = con.cursor()
  
   cur.executemany("UPDATE cars SET x=?,y=? WHERE z=?",(x,y,z))
   con.commit()
   
   cur.execute("SELECT * FROM cars")
   ROW =cur.fetchall()
   for row in ROW:
      print(row)
