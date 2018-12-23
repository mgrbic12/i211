import urllib.request
import re
import random
import webbrowser
import os
#Wiki browsing pt 2
#Modify our link-finder v1 code to stimulate browsing random links on wikipedia using what we learned in pt: 

##def browser(url):
##     web_page = urllib.request.urlopen(url)
##     lines = web_page.read().decode(errors="replace")
##     web_page.close()
##     body = re.findall('(?<=<body).+?(?=</body>)', lines, re.DOTALL)[0]
##     hits = re.findall('(?<=href=").+?(?=")', body)
##     wiki_links = [link for link in hits if "wiki" in link and ".org" not in link]
##     return wiki_links

def image_list(url):
    pages = urllib.request.urlopen(url)
    lines = pages.read().decode(errors = "replace")
    pages.close()
    body = re.findall('(?<=<body).+?(?=</body>)', lines, re.DOTALL)[0]
    images = re.findall('(?<=img src=").+?(?=")',body)
    for item in images:
        urllib.request.urlretrieve(item, os.path.basename(item))




##
##
###body
##    
##user_web = input("Where would you like to start?: ")
##user_jumps = eval(input("How many jumps?: "))
##
##web_list = browser(user_web)
##
##count = user_jumps
##
##for i in range(count):
##    random_choice = random.choice(web_list)
##    link = "http://en.wikipedia.org" + random_choice
##    print("Jumping from: ", user_web)
##    webbrowser.open(link)
##    print("To: ", link)
##    user_web = link
##    web_list = browser(link)
    
###
#body for image_list()
image_list("https://www.sice.indiana.edu/news/index.html")

