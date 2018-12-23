#! /usr/bin/env python3
print('Content-type:text/html\n')
import MySQLdb
import cgi

string = "i211f18_mgrbic"
password = 'my+sql=i211f18_mgrbic'

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port=3306, user=string, passwd=password, db=string)

cursor= db_con.cursor()
form = cgi.FieldStorage()

html = """
<html>
<head>
<title>Faculty Table</title>
</head>
<body>
<table border="1" width="30%">
<tbody>
	<tr>
		<th>Faculty</th>
		<th>Name</th>
		<th>Title</th>
		<th>Email</th>
		<th>Areas</th>
	</tr>
	{table}
</tbody>
</body>
</html>"""

name = form.getfirst('name','jack')
title = form.getfirst('title', 'teacher')
email = form.getfirst('email', 'jack@iu.edu')
areas = form.getfirst('areas','Informatics')

SQL_add = "INSERT INTO Faculty (Name, Title, Email, Areas)"
SQL_add += "VALUES('" + name + "','" + title + "','" + email + "','" + areas+ "');"
cursor.execute(SQL_add)
db_con.commit()

SQL = "SELECT * FROM Faculty;"
cursor.execute(SQL)
results = cursor.fetchall()

final = ""
for row in results:
	final += "<tr>"
	for elem in row:
		final += "<td>" + str(elem) + "</td>"
	final += "</tr>"

print(html.format(table = final))
