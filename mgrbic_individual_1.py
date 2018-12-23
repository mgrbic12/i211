#Max Grbic
#mgrbic
#Lecture Team Number : 14


#Rock, Paper, Scissors algorithm


#Import Random Module


#set random choice of Rock, Paper, or Scissors to 'comp_try'


#Prompt user to choose 'Rock, Paper, or Scissors' and set to 'user_try'


#check if 'user_try' is 'Rock'
    #if so, is 'comp_try' equal to 'Rock'
        #Print message "Tied"

    #if so, is 'comp_try' equal to 'Paper'
        #Print message "Lost"

    #if so, is 'comp_try' equal to 'Scissors'
        #Print message "Won"


#check if 'user_try' is 'Paper'
    #if so, is 'comp_try' equal to 'Rock'
        #Print message "Won"

    #if so, is 'comp_try' equal to 'Paper'
        #Print message "Tied"

    #if so, is 'comp_try' equal to 'Scissors'
        #Print message "Lost"


#check if 'user_try' is 'Scissors'
    #if so, is 'comp_try' equal to 'Rock'
        #Print message "Lost"

    #if so, is 'comp_try' equal to 'Paper'
        #Print message "Won"

    #if so, is 'comp_try' equal to 'Scissors'
        #Print message "Tied"


#End game, ask if they would like to play again
    #if yes, Repeat

#additional comments: The algorithm checks to see what the user has used for input (Rock, Paper, or Scissors).
#From there we the algorithm can determine the outcome based upon what the computer randomly generated. This is done by simple comparison of the two choices
##################################################

#3.) Write a program that asks the user as a string as the input. It should duplicate all the characters in the string and print it back out to the user

user_string = input("Enter a string :")

new_string = ""

for char in user_string:
    new_string += char + char
    

print(new_string)

#additional comments: The program takes a user input. From there it runs through a for loop that looks at all the characters (char).
#Inside the for loop we are adding the new contents of char + char (which duplicates the specific character), and adding it into an empty list
#outside if the for loop
###################################################

#4.) Write a program that takes two lists and displays 'True', if they atleast have one member in common, 'False' otherwise.
lst_1 = ['k', 'b', 'c', 'd', 'e', 'f', 'g']
lst_2 = ['a', 'h', 'i', 'j', 'k', 'l', 'm']

result = False

for i in lst_1:
    for j in lst_2:
        if i == j:
            result = True
print(result)
print(lst_1)
print(lst_2)

#additional comments: Initially tried to return False if i was not equal to j. However, pything kept sending me
#an error that the return was outside the function
# Thought about storing the boolean variable inside a variable that would change if a certain condition was met (if i ==j).
#then I would just print the variable depending if the condition was met








