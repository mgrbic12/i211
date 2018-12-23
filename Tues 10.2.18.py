import re
import urllib.request


#Redaction - write a program to read a file and save a copy of the file with all emails, phone numbers,
#and proper names replaced with the word "redacted"

##test = open("message.txt", "r")
##contents = test.read()
##test.close()
##
##redacted = re.sub('[\w]+@[\w]+.[\w]+|[(][\d]{3}[)] [\d]{3}-[\d]{4}|[A-Z][\w]+ [A-Z][\w]+', "redacted", contents)
##
##new_file = open("messageRedacted", "w")
##new_file.write(redacted)
##new_file.close()
##
##print(redacted)

#Url Finder - Write a program to parse a webpage and return all the links on it using regular expressions

sice_url = "http://www.sice.indiana.edu/about/contact/index.html"

print("Searchings:", sice_url)

web_page = urllib.request.urlopen(sice_url)
contents = web_page.read().decode(errors = "replace")
web_page.close()

test = contents

urls = re.findall('(?<=href=").+?(?=")',test)

for item in urls:
    print(item)
