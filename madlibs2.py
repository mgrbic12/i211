#! /usr/bin/env python3
print('Content-type:text/html\n')

import cgi

html"""<h1>A day in my favorite course: I211</h1>
<p>As a <em>{0}</em>, I always make sure to arrive early so I can get the best <em>{1}</em>.</p>
<p>Next to arrive is my group member, <em>{2}</em>, who goes by <em>{3}</em>, and is always telling jokes about <em>{4}</em>. Always makes me <em>{5}</em>.</p>
<p>When class begins, I <em>{6}</em> <em>{7}</em>. This shows that I'm paying attention.</p>
<p>We start to work on the first problem, and I wave my <em>{8}</em> to let the AI know I have a question. My AI tells me that a <em>{9}</em> in my code is causing an error.</p>
<p>The problems are <em>{10}</em>, but my team is <em>{11}</em> and we make it through.</p>
<p>Class ends and we all go to <em>{12}</em> to get a <em>{13}</em>... <em>{14}</em>, I just love I211!</p>"""

variable0 = form.getfirst('rank', 'junior')
variable1 = form.getfirst('furniture', 'seat')
variable2 = form.getfirst('person','max')
variable3 = form.getfirst('nickname', 'skippy')
variable4 = form.getfirst('objects', 'pandas')
variable5 = form.getfirst('expression', 'cry')
variable6 = form.getfirst('verb', 'sit')
variable7 = form.getfirst('thing1', 'upright')
variable8 = form.getfirst('body_part', 'hand')
variable9 = form.getfirst('thing2', 'bug')
variable10 = form.getfirst('adj1','tough')
variable11 = form.getfirst('adj2','persistant')
variable12 = form.getfirst('place','Starbuck')
variable13 = form.getfirst("drink","coffee")
variable14 = form.getfirst("exclamation","golly")

print(html.format(variable0, variable1, variable2, variable3, variable4, variable5, variable6, variable7, variable8, variable9, variable10, variable11, variable12, variable13, variable14))


