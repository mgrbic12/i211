#Max Grbic
#Group 14
#Assignment 6
import re
import urllib.request

#1.)Write a python regular expression that would match a hex color code.
#regular expression to match a hex color: ('#[\w]{6}')



#2.)Write an algorithm for step 3. As part of your algorithm, be sure to describe the pattern you're using to find the win/loss result of each game
#import urllib.request
#create variable name and use : urllib.request.urlopen("")
#Create variable and read in contents with .read()
#Close page
#Create regular expression to match all games
####regex : ('(?<=<div class='schedule_game_results'><div>).+?(?=</div>)', "variable name", re.DOTALL)
#Create a list for each wins and losses
#use a for loop to iterate over the list and if the item has a "W" or "L", append it to correct list
#print the results by using len

#############
#went to office hours and was not able to do the simple div tag when looking ahead and behind
#Then I attempted the extended div tag that comes before the scores and that worked




#3.)Write a program at the source (###). Use regular expressions to find all the games IU has played this year and calculate the total number of wins and losses.
web_page = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/mbball.html")
lines = web_page.read().decode(errors = "replace")
web_page.close()

scores = re.findall("(?<=<div class='schedule_game_results'><div>).+?(?=</div>)", lines, re.DOTALL)


W_list = []
L_list = []


#Adding the appropriate final scores to the corresponding list
for item in scores:
    if "W" in item:
        W_list.append(item)

for item in scores:
    if "L" in item:
        L_list.append(item)


print("Wins:", len(W_list))
print("Losses:", len(L_list))

#taking the len() will give me the amount that is in the list
#This works because we separate each final score indicated on whether it was a win or loss

#Bonus, total difference
##print(W_list)
##for item in W_list:
##    num = item
##    diff = int(10 * num[2]) + int(num[3])
##print(diff)


    
