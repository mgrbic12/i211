#Max Grbic
#Lecture/Lab Group # 14/4
import random

#Write a program that implements the word guessing game (hangman) we wrote an algorithm for in lecture 2.

secrete_words = ["python", "code", "informatics"]

secrete = random.choice(secrete_words)

wrong_guess = 0

unknown = ['_' * len(secrete)]

rev_letters = []

print("Guess the secrete word!:", unknown, '\n')

while True:
    user_letter = input("Please enter a letter guess for the secrete word!: ")
    hangman_str = ""
    
    if user_letter in secrete:
        rev_letters.append(user_letter)
        print("Correct!")
        
    else:
        wrong_guess += 1
        print("Wrong answer!")

    for letter in secrete:
        if letter == user_letter:
            hangman_str += user_letter
        elif letter in rev_letters:
            hangman_str += letter
        else:
            hangman_str += "_"
    if hangman_str == secrete:
        break
    
    elif wrong_guess == 3:
        break

print("The word was!:", hangman_str)

            




#Write a program that implements the rock, paper, scissors game.

##RPG_game = ["Rock", "Paper", "Scissors"]
##
##while True:
##    comp_try = random.choice(RPG_game)
##    user_try = input("Please choose between 'Rock', 'Paper', 'Scissors' (or 'STOP'): ")
##    
##    if user_try.upper() == "STOP":
##        print("Thanks for playing!")
##        break
##    
##    if user_try == "Rock":
##        print("You: " + user_try, "vs.", "Them: " + comp_try)
##        if comp_try == "Rock":
##            result = "Tied"
##        if comp_try == "Paper":
##            result = "Lost!"
##        if comp_try == "Scissors":
##            result = "Won!"
##        print(result)
##        
##
##    if user_try == "Paper":
##        print("You: " + user_try, "vs.", "Them: " + comp_try)
##        if comp_try == "Rock":
##            result = "Won!"
##        if comp_try == "Paper":
##            result = "Tied"
##        if comp_try == "Scissors":
##            result = "Lost"
##        print(result)
##
##    if user_try == "Scissors":
##        print("You: " + user_try, "vs.", "Them: " + comp_try)
##        if comp_try == "Rock":
##            result = "Lost"
##        if comp_try == "Paper":
##            result = "Won!"
##        if comp_try == "Scissors":
##            result = "Tied"
##        print(result)





