import sqlite3 as a
import sys #system
cars=( (1,'mercedes',745612),(2,'audii',747534),(3,'bugatti',74561200),(4,'nano',45612),(5,'tesla',74561211),(6,'nexa',7456122))
con = a.connect('cars.db')
with  con:
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS cars")
   cur.execute("CREATE TABLE cars (id INT,Name TEXT, Price INT)")
   cur.executemany("INSERT INTO cars VALUES(?,?,? )",cars)
   
   
   
