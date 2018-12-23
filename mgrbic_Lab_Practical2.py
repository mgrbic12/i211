#Max Grbic
#Group 14
#Lab Practical 2

#################

#imports
import re
import urllib.request
import webbrowser



#Section 1 - Website
#The url to website: https://www.indiana.edu/news-events/index.html
#use urllib.request to open the webpage, read in the contents, then close


web_page = urllib.request.urlopen("https://www.indiana.edu/news-events/index.html")
lines = web_page.read().decode(errors="replace")
web_page.close()


#Section 2 - News Articles
#produce out for all of the news articles on the page
#using re.findall and .+? I am able to extract all contents inside the specified 'lookbehind' and 'lookahead' criteria.
#To print the output accordingly, use a for loop and add a new line after each print


print("Searching: https://www.indiana.edu/news-events/index.html\n")

article = re.findall('(?<=span itemprop="headline">).+?(?=</span>)',lines,re.DOTALL)

for item in article:
    print(item, "\n")



#section 3 - headline matching
#user input for phrase

    
print("-" * 70) #for better look of output

user_in = input("Please enter a word to search for: ")
print() #for better look of output

for elem in article:
    if user_in.upper() in elem.upper():
        print(elem, "\n")



#section 4 - Bonus|Web browsing
#used regex to search for links in the content
#extraced the non necessary links that were matched and put them in a list
#then used a for loop to iterate through each piece and see in user input mathed
#If so then opened a new tab



web_browse = re.findall('(?<=<a itemprop="url" href=").+?(?=">)',lines, re.DOTALL)

final_links = []

for item in web_browse:
    if "https://apps." not in item:
        final_links.append(item)


for url in final_links:
    if user_in in web_browse:
        webbrowser.open_new_tab(url)
