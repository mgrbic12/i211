#! /usr/bin/env python

import cgi

print('Content-type: text/html\n')

html = """
<html>
	<head>
		<title>Alphabet Practie</title>
		<body>
			<img src="{image}">
			<h2>{answer}</h2>
			<form method="post" action="pxqzj.cgi">
            <p>The letter:
            <select name="letter">
                <option>a</option>
                <option>b</option>
                <option>c</option>
                <option>d</option>
                <option>e</option>
                <option>f</option>
                <option>g</option>
                <option>h</option>
                <option>i</option>
                <option>j</option>
                <option>k</option>
                <option>l</option>
                <option>m</option>
                <option>n</option>
                <option>o</option>
                <option>p</option>
                <option>q</option>
                <option>r</option>
                <option>s</option>
                <option>t</option>
                <option>u</option>
                <option>v</option>
                <option>w</option>
                <option>x</option>
                <option>y</option>
                <option>z</option>
            </select>
            </p>
            <p>Is for: <input type="text" name="guess"></p>
        <button type="submit">Submit</button>
</form> 
		</body>
	</head>
</html>"""

form = cgi.FieldStorage()

letter = form.getfirst('letter','a')
guess = form.getfirst('guess','Han Solo')

char_dict = {'a':"Ackbar", "b":"Bossk", "c":"Chewie and C-3PO", "d":"Dash Rendar", "e":"Ewoks", "f":"Fett", "g":"Greedo", "h":"Han Solo", "i":"IG-88", "j":"Jabba", "k":"Kyle Katarn", "l":"Luke and Leia", "m":"Mara Jade", "n":"Nien Nunb", "o":"Obi-Wan", "p":"Palpatine", "q":"Quinian Vos", "r":"R2-D2", "s":"Storm Troopers", "t":"Thrawn", "u":"Ulic Qel-droma", "v":"Vader", "w":"Wedge", "x":"Xizor", "y":"Yoda", "z":"Zuckuss"}

if guess == char_dict[letter]:
	reply = "That's Correct!"
else:
	reply = "Sorry, the correct response was" + " " + char_dict[letter]

print(html.format(answer = reply, image = "vrtpr/" + letter + ".jpg"))