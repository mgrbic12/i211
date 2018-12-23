#Algorithm file space:

#import os

#While directory

#for loop in current directory

#if there is a file

###add bytes size to counter

#if there is sub directory

###for loop in subdirectory

#if file

###add byte size to counter

#print counter

#############################################
#file_space(code)

##import os
##
##def file_size(dir):
##    total = 0
##    for item in os.listdir(dir):
##        if os.path.isfile(item):
##            total += os.path.getsize(item)
##        elif os.path.isdir(item):
##            total += file_size(os.path.join(dir,item))
##    return total
##
###Main
##start = input("Please enter a file location: ")
##os.chdir(start)
##allsize = file_size(os.getcwd())
##print("The total size for all files in", start, "is", allsize, "bytes")

#############################################
#datetime module

##import datetime
##
##now = datetime.date(2015, 1, 1)
##print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B"))

#########

##now = datetime.date.today()
##birthday = datetime.date(1997, 10, 7)
##age = now - birthday
##print("I am", age.days, "days old.")
##print("Which is", age.days / 365, "years old.")

###################################################
###time module
##
##import time
##start = time.clock()
##
##for i in range(250):
##    print(i)
##
##end = time.clock()
##
##print("\nTotal time:", end - start, "seconds")

#####################################################
#day finder
import random
import datetime
import time

start = time.clock()

while True:
    month = random.randrange(1, 13)
    year = random.randrange(1900, 2001)
    day = random.randrange(1,32)
    try:
        date = datetime.date(year, month, day)

    except:
        print("Invalid date")
        
    else:
        print(date.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B"))
    

        if date.strftime("%A") == "Thursday" and date.strftime("%B") == "February" and ((year) % 7) == 0:
            print(date.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B"))
            break
    

end = time.clock()
print("\nTotal time:", end - start, "seconds")


