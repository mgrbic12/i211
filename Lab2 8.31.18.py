##4 letter word game
##def getGuess(user_guess):
##    random_word = "code"
##    score = 0
##
##    if user_guess in random_word:
##        score += 1
##        return score
##    else:
##        print("Incorrect")
##
####    while True:
####        if user_guess in random_word:
####            score += 1
####            return score
####            if score == 4:
####                print("You win!")
####                break
####        else:
####            print("Letter not in word!")
##
##        
##
##
##
##
##
##
##
##
###main
##
##while getGuess < 4:
##    user_guess = input("Please enter a letter guess: ")
##    
##            
##
##
##print(getGuess(user_guess))



##################################################



##data = ['50 apples\n', '25 pears\n', '10 oranges\n']

#Add 'data' to nested list

##groceries = []
##
##for item in data:
##    number, fruit = item.strip().split(' ')
##    groceries.append([number, fruit])
##    
##
##print(groceries)
##print("The number of oranges are: ", groceries[2][0])


#Add 'data' to dictionary

##groceries = {}
##
##for item in data:
##    number, fruit =item.strip().split(' ')
##    
##    groceries[fruit] = int(number)
##
##print(groceries)
##print("The number of oranges is: ",groceries["oranges"])

