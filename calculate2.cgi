#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()
html = """<!doctype html>
<html>
    <head>
	   <meta charset="utf-8">
	   <title>Form in CGI</title>
    </head>
    <body>
	   <p>{content}</p>
    </body>
</html>"""

total = 1
user = form.getfirst('speech','none')
if form.getfirst('math') == "Add":
    new_user = user.split('/r/n')
    total = sum(new_user)
else:
    new_user = user.split('/r/n')
    for item in new_user:
        total *= item

print(html.format(content = 'The sum is: ' + total))
