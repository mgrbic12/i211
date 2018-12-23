#! /usr/bin/env python3
print('Content-type:text/html\n')
import MySQLdb

string = "i211f18_mgrbic"
password = 'my+sql=i211f18_mgrbic'

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port=3306, user=string, passwd=password, db=string)

cursor= db_con.cursor()

try:
	SQL = "SHOW Tables;"
	cursor.execute(SQL)
	results = cursor.fetchall()
	
except Exception as e:
	print('<p>Something went wrong with the SQL!</p>')
	print(SQL, "Error:",e)
	
else:
	result = ""
	for row in results:
		for item in row:
			result += item + '<br>'
	print(result)