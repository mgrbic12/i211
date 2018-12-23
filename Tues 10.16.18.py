import xml.etree.ElementTree as ET


#Write a function called 'id_find(num)' that takes an id number as a string and returns the name of the students who matches that id.

##def id_find(num):
##    root = ET.parse(source="students.xml")
##    elements = root.findall("Student")
##
##    for elem in elements:
##        if elem.find("id").text == num:
##            first = elem.find("name/first").text
##            last = elem.find("name/last").text
##            name = first + " " + last
##            return name
##    return "Not Found"


#Write a function called 'fee_find(name)' that takes a student's name as a string and returns the fee information about that student
def fee_find(name):
    root = ET.parse(source="students.xml")
    elements = root.findall("Student")

    for elem in elements:
        if elem.find("name/first").text + " " + elem.find("name/last").text == name:
            fee = elem.find("fees")
            fees_sentence = name + ' ' + "owes" + ' ' + fee.text +' '+ fee.attrib['c'] + ' ' + fee.attrib['units']
            return fees_sentence
    return "Not Found"
    



###main
##print(id_find("0019846768"))
##print(id_find("0019846789"))
##print(id_find("1234567890"))


#main2
print(fee_find("Rose Dawson"))
print(fee_find("Jack Sparrow"))
print(fee_find("No Body"))
