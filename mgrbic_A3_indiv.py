#Max Grbic
#Lecture/lab group number : #14/4
####################################

#Algorithm to solve steps:

#1.)Prompt user input for filename
#2.)Read in filename with list comprehension
#3.)Create data into dictionary
#4.)Print out data in prompted format
#5.)Create list comprehension for teams with letters less than 5
#6.)create list comprehension for three teams with most wins
#7.)Print out reults


#Reading in the file from user input

file_name = input("Please enter a file name: ")

file_contents = [line.strip() for line in open(file_name, "r")]

#Creates a dictionary with given data

teams = {}
for item in file_contents:
    team, wins = item.split(" ")
    teams[team] = int(wins)

#Used to print out the teams with their corresponding wins

for squads in teams:
    print("The", squads, "have won", teams[squads], "games")

#Teams with names shorter than 5 letters

letters_less = [team for team in teams if len(team) < 5]
print("\nTeams with names shorter than 5 letters: ", letters_less)

#Three teams with most wins

most_wins = [team[0] for team in teams.items() if int(team[1]) > 6]
print("\nThe three teams with the most wins are: ", most_wins)



