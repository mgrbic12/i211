#Individual LC

##doubles = [x * 2 for x in range(10)]
##print(doubles)

################################################

#Individual LC

##numbers = [x for x in range(100) if x % 10 == 0]
##print(numbers)

#################################################
#Individual LC

##words = ["apple", "ball", "candle", "dog", "egg", "frog"]
##
##new_words = [words[i].upper() if len(words[i]) < 4 else words[i] for i in range(len(words))]
##print(new_words)
##
##
##new_list = [words[i].upper() for i in range(len(words)) if len(words[i]) < 4]
##print(new_list)


#################################################

user_input = input("Please enter the secrete: ")

redacted = "".join(["-" if ch.isalpha() else ch for ch in user_input])
print(redacted)
