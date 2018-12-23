#! /usr/bin/env python3
print('Content-type:text/html\n')

import cgi
import random

html = """
<!doctype html>
<html>
<head><meta charset = "utf-8">
<title>Form in CGI</title>
    <body>
    <p> You guessed: <img src="{pic}" height = "300"></p>
    <p> Computer guessed: <img src="{comp}" height = "300"></p>
    <p>{message}</p>
    </body>
</html>"""

rps_dict = {"rock":"rps_pictures/rock.jpg", "paper":"rps_pictures/paper.jpg", "scissors":"rps_pictures/scissors.jpg"}

message = ""

form = cgi.FieldStorage()
user = form.getfirst("symbol", "rock")


game_options = ["paper","rock","scissors"]

computer_move = random.choice(game_options).lower()

if user == computer_move:
    message = "Its a Tie..."
elif user == "scissors":
    if computer_move == "rock":
        message = "Computer Wins "
    else:
        message = "You Win!"
elif user == "paper":
    if computer_move == "scissors":
        message = "Computer Wins "
    else:
        message = "You Win!"
elif user == "rock":
    if computer_move == "paper":
        message = "Computer Wins "
    else:
        message = "You Win!"
else:
    message = "Invalid answer. Retry"

    


print(html.format(pic = rps_dict[user], comp = rps_dict[computer_move], message = message))
