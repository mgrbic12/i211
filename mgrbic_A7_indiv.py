#Max Grbic
#Group 14
#Individual 7

import xml.etree.ElementTree as ET

#Write a program to read the file and print out the following information with an appropriate message:

#1.)Write a function called display_book that prints the title, author, and price of the book with certain id (passed as a parameter)
#ex: display_book("bk107")
def display_book(book_id):
    root = ET.parse(source="library.xml")
    book = root.iter("book")
    
    for elem in book:
        if elem.attrib['id'] == book_id:
            print("The title is:", elem.find("title").text)
            print("The author is:", elem.find("author").text)
            print("The price is:", elem.find("price").text)
            print("-" * 40)
        

#main
book_id = input("Enter the book 'id' you wish to know about: ")
print("-" * 40)
display_book(book_id)



#2.)Display the title, author, and price of each Computer book released in December
root = ET.parse(source="library.xml")
book = root.iter("book")

for elem in book:
    if elem.find("publish_date").text[5:7] == "12" and elem.find("genre").text == "Computer":
        print(elem.find("author").text)
        print(elem.find("title").text)
        print(elem.find("price").text)
    
print("-" * 40)



###3.)Print all the genres in the file
genres = root.findall("book/genre")

total_genres = []
for item in genres:
    if item.text not in total_genres:
        total_genres.append(item.text)
        
print("All the genres are:\n")

for elem in total_genres:
    print(elem)





