import re
import urllib.request, os

##read_file = open("quote.txt","r")
##file_contents = read_file.read()
##read_file.close()
##
##print("Words beginning with a capital letter:", re.findall('[A-Z]+[\w]*', file_contents))
##print()
##print("Words enging in 'ing':", re.findall('[\w]*ing', file_contents))
##print()
##print("Words with two 'a's in them:", re.findall('[\w]*a[\w]*a[\w]*', file_contents))
##print()
##print("Phrases that begin and end with a comma:", re.findall(',[^.?`,]*,', file_contents))
##print()
##print("The number of words that begin with the letter 'v':", len(re.findall('[vV][\w]*', file_contents)))

##counter = 0
##
##for item in words:
##    if item:
##        counter+=1
##
##print("The number of words that begin with the letter 'v':", counter)\

######################################################


web_page = urllib.request.urlopen("http://www.soic.indiana.edu/about/contact/index.html")
lines = web_page.read().decode(errors = "replace")
web_page.close()

test = lines

phones = re.findall('[(][\d]{3}[)] [\d]{3}-[\d]{4}',test)

for item in phones:
    print(item)


