#Max Grbic
#Lecture group #14
###################

import csv
import datetime

#1.) When using strftime what is the placeholder that will display the full name of the day of the week.
#When using strftime the placeholder that will display the full name of the day of the week is %A.
#%A

#2.) Write an algorithm for step 3
#Import correct modules / csv and datetime
#open contents of csv file with DictReader
#For loop to iterate over contents
#Split contents of the date
#Arrange order of the date to different format for year, month, day
#conditional statements to determine if the day is a weekend
#print items that fulfill the conditonal statements




#3.)Write a program that reads in the information from a file called ShopRecords.csv and displays all the items that were sold on a weekend.
shop_records = csv.DictReader(open("ShopRecords.csv", "r"))

for entry in shop_records:

    item_date = entry["Date"].split("/")
    date = datetime.date(int(item_date[2]), int(item_date[0]), int(item_date[1]))
    
    if date.strftime("%A") == "Saturday" or date.strftime("%A") == "Sunday":
        print(entry["Item"])






