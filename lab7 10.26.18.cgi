#! /usr/bin/env python3

print('Content-type: text/html\n')


moviesRT = open("top100moviesRT.txt", "r")
RTcontents = moviesRT.readlines()
moviesRT.close()

moviesAFI = open("top100moviesAFI.txt", "r")
AFIcontents = moviesAFI.readlines()
moviesAFI.close()

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Top Movie Comparison</title>
</head>
<body>
    <h1>Top 100 Film Comparisons</h1>
	<table border = 1><tr><td>Movie</td><td>AFI Rank</td><td>RT Rank</td></tr>
	{content}</table>
</body>
</html>"""

table = ""

##<td rowspan=2> "cell value"</td>




for item in sorted(set(RTcontents) | set(AFIcontents)):
    if item in RTcontents:
        RT_rank = RTcontents.index(item)
        
    else:
        RT_rank = "--"

    if item in AFIcontents:
        AFI_rank = AFIcontents.index(item)
        
    else:
        AFI_rank = "--"
        
    table += "<tr><td>" + item + "</td><td>" + str(AFI_rank) + "</td><td>" + str(RT_rank) + "</td></tr>"


print(html.format(content = table))
        

    


