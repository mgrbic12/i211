out = open("template2.html", "w")

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hello</title>
</head>
<body>
	{content}
</body>
</html>"""

name = input("Please enter your name: ")
message="hello" + name

out.write(html.format(content=message))
out.close()

print("Finished writing.")

