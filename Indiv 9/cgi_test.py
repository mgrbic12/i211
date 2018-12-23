#! /usr/bin/env python3
print('Content-type:text/html\n')

import cgi

form = cgi.FieldStorage()
html = """
<!dotype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Robot Delivery System Confirmation</title>
	</head>
	<body>
		<h1>Robot Delivery Confirmation</h1>
		<p>You have selected to have a {order} delivered by {delivery}.</p>
		<p>Your total comes to ${final}</p>
	</body>
</html>"""

method = form.getfirst('delivery_method' ,'drone')
order = form.getfirst('delivery','pizza')
price = form.getfirst('cost','5')

total = 0

if method == "drone":
	total += 10
if method == "self driving car":
	total += 20
if method == "giant robot":
	total += 1000
	
total += float(total)
new_total = str(total)

print(html.format(order = order, delivery = method, final = new_total))
