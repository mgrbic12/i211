#! /usr/bin/env python3
print('Content-type:text/html\n')
import MySQLdb

string = "i211f18_mgrbic"
password = 'my+sql=i211f18_mgrbic'

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port=3306, user=string, passwd=password, db=string)

cursor= db_con.cursor()

try:
	#SQL = """CREATE TABLE Student
	#(StudentID int UNIQUE NOT NULL,
	#Name varchar(25) NOT NULL,
	#Major varchar(100) NOT NULL,
	#Email varchar(30),
	#Credits int);"""
	SQL = "SELECT * FROM Student;"
	
	cursor.execute(SQL)
	results = cursor.fetchall()
	
except Exception as e:
	print('<p>Something went wrong with the SQL!</p>')
	print(SQL, "Error:",e)



else:
	print(results)

try:
	SQL2 = """INSERT INTO Student
	VALUES(1,'Max', 'Informatics', 'mgrbic@iu.edu', 90),
	(2, 'Bob', 'English', 'bobby@iu.edu', 85),
	(3, 'Tim', 'Math', 'timmy@iu.edu', 70);"""
	
	cursor.execute(SQL2)
	db_con.commit()
	results_2 = cursor.fetchall()
	
except Exception as e:
	print('<p>Something went wrong with the SQL!</p>')
	print(SQL, "Error:",e)

else:
	print("Entries added!")

