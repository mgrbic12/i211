#! /usr/bin/env python

import cgi

print('Content-type: text/html\n')

html = """
<html>
<body>
	<table>
		<tbody>
			<tr>
				<td>
					<h1>You guessed:</h1>
					<img src="{image}">
				</td>
			</tr>
			<tr>
				<td>
					<h1>Suit:</h1>
					{suit}
				</td>
			</tr>
			<tr>
				<td>
					<h1>Rank:</h1>
					{rank}
				</td>
			</tr>
		</tbody>
	</table>
	{again}
</body>
</html>"""

form = cgi.FieldStorage()

suit_guess = form.getfirst('suit', 'D')
rank_guess = form.getfirst('rank', '2')

our_guess = "10S"

rank_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}

if suit_guess == "S":
	suit_reply = "Correct Suit!"
else:
	suit_reply = "Wrong Suit!"


if rank_dict[rank_guess] < rank_dict["10"]:
	rank_reply = "Too Low!"
	
if rank_dict[rank_guess] > rank_dict["10"]:
	rank_reply = "Too High!"

if rank_dict[rank_guess] == rank_dict["10"]:
	rank_reply = "Correct Rank!"

if suit_reply == "Correct Suit!" and rank_reply == "Correct Rank!":
	new_game = "Nice Job!"
else:
	new_game = """<form method="post" action="guessmycard.cgi">
	<H2>Try to guess the card!</H2>
	<p>Rank:
		<select name="rank">
			<option>2</option>
			<option>3</option>
			<option>4</option>
			<option>5</option>
			<option>6</option>
			<option>7</option>
			<option>8</option>
			<option>9</option>
			<option>10</option>
			<option>J</option>
			<option>Q</option>
			<option>K</option>
			<option>A</option>
		</select>
	</p>
	<p>Suit:
		<br /><input type="radio" name="suit" value="C" checked />Clubs
		<br /><input type="radio" name="suit" value="D" />Diamonds
		<br /><input type="radio" name="suit" value="H" />Hearts
		<br /><input type="radio" name="suit" value="S" />Spades
	</p>
	<button type="submit">Submit</button>
	<button type="reset">Reset</button>
</form>"""
	

image_fill = "cards/" +rank_guess + suit_guess +".jpg"

print(html.format(image = image_fill, suit = suit_reply, rank = rank_reply, again = new_game))








