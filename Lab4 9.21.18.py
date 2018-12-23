import csv
import datetime

def getBIOS():
    print("-" * 50)
    print("BIOS")
    print("-" * 50)

    bio_info = csv.DictReader(open("star-wars.csv", "r"))
    
    youngest = ["",100]
    
    oldest = ["",0]
    
    now = datetime.date.today()
    
    friday = []
    
    
    for item in bio_info:
        dob = now.strftime("%A, %b %d, %Y")
        bday = item["birthday"].split("/")
        birthday = datetime.date(int(bday[2]), int(bday[0]), int(bday[1]))
        age = now - birthday
        if birthday.strftime("%A") == "Friday":
            friday.append(item["name"])
        
        
        age_2 = int(age.days/365)
        if youngest[1] > age_2:
            youngest[1] = age_2
            youngest[0] = item["name"]

        if oldest[1] < age_2:
            oldest[1] = age_2
            oldest[0] = item["name"]
            


        print(item["character"], "is played by", item["name"] + ",\n", "who was born on", dob + ".\n", item["name"], "is", str(int(age.days/365)), "years old.")
        print("\n")
        
    print("The oldest cast member is", oldest[0], "who is", oldest[1], "years old.")
    print("The youngest cast member is", youngest[0], "who is", youngest[1], "years old.")
    print("\n")
    print("Cast members born on a friday:")
    for ppl in friday:
        print(ppl)




    

            
        





def listCharacters():
    print("-" *40)
    print("MAIN CHARACTERS")
    print("Star Wars: Episode VII: The Force Awakens (2015)")
    print("-" * 40)

    people = csv.DictReader(open("star-wars.csv", "r"))
    

    for entry in people:
        pad_1 = 50 - len(entry["character"])
        pad_2 = 50 - len(entry["name"])
        
        print(entry["character"], " " * pad_1, entry["name"], " " * pad_2, entry["birthday"])

#main
##listCharacters()
getBIOS()
