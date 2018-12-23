#! /usr/bin/env python3
print('Content-type:text/html\n')
import cgi
form = cgi.FieldStorage()

import random
import MySQLdb

string = "i211f18_mgrbic"
password = 'my+sql=i211f18_mgrbic'

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port=3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

def get_weapon(cursor, winner):
	try:
		SQL = "SELECT * FROM Robot WHERE Name = '"+winner+"';"
		cursor.execute(SQL)
		weapon = cursor.fetchall()[0][0]
	except:
		weapon="something went wrong with SQL"
	return weapon
	
def deactivate(cursor, dead_robot):
	try:
		SQL = "UPDATE Robot SET Active = 'False' WHERE Name = '"+dead_robot+"';"
		cursor.execute(SQL)
		db_con.commit()
	except:
		print("Row not deleted!")

def robot_fight(cursor, robot1, robot2):
	botlist = [robot1, robot2]
	winner = botlist.pop(random.randint(0,1))
	loser = botlist[0]
	output= str(winner) +"wins the round with its" +str(get_weapon(cursor, winner))+'.<br>'
	output +=str(loser) + "is now deactivated."
	deactivate(cursor,loser)
	return output

###main###
html = """
<html>
	<head>
		<title>Robot Fight!</title>
	</head>"""

try:
	SQL = "SELECT Name FROM Robot;"
	cursor.execute(SQL)
	names = cursor.fetchall()
except Exception as e:
	print('<p>Something went wrong with the SQL!</p>')
	print(SQL, "Error:", e)
else:
	if not form.getfirst("robot1", None):
		html += """<body>
		<h1>Choose two robots to face off!</h1>
		<form method="post" action="robot_fight.cgi">
		<h3>Please select robots:</h3>
		<p>Robot Name:
		<select name="robot1">"""

for name in names:
	html +="<option>"+name[0]+"</option>"
	html+="""</select></p>
	<input type="submit" value="Fight!"/>
	</form>
	"""
else:
	robot1 = form.getfirst("robot1")
	robot2 = form.getfirst("robot2")
	html += robot_fight(cursor,robot1,robot2)
html += """</body>
</html>"""
print(html)
