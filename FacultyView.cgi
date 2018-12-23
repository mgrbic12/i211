#! /usr/bin/env python3
print('Content-type:text/html\n')
import MySQLdb

string = "i211f18_mgrbic"
password = 'my+sql=i211f18_mgrbic'

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port=3306, user=string, passwd=password, db=string)

cursor= db_con.cursor()

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
		<th>Edit</th>
		<th>Delete</th>
	</tr>
	{table}
</tbody>
</body>
</html>"""

SQL = "SELECT * FROM Faculty;"
cursor.execute(SQL)
results = cursor.fetchall()

final = ""
for row in results:
	final += "<tr>"
	for elem in row:
		final += "<td>" + str(elem) + "</td>"
	final += "<td>" + "<a href='FacultyDelete.cgi?fid=" + str(row[0]) + "'>Delete</a></td>"
	final += "<td>" + "<a href='FacultyEdit.cgi?fid=" + str(row[0]) + "'>Edit</a></td>"
	final += "</tr>"

print(html.format(table = final))