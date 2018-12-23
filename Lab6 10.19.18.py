import xml.etree.ElementTree as ET

root = ET.parse(source="cd_catalog.xml")

cd = root.iter("CD")

#CD num
cd_num = 0
for item in cd:
    if item:
        cd_num += 1

print("The total number of CD's in the file:", cd_num)
####################
#total cd price
price = root.findall("CD")

total_price = []

for elem in price:
    total_price.append(float(elem.find("PRICE").text))
final_price = sum(total_price)

print("The total price of purchasing one of each is:", round(final_price, 2))

#####################
#min, max, and average

print("\nThe maximum price:", max(total_price))
print("The minimum price:", min(total_price))
print("The average price:", round((final_price / len(total_price))))
print()
####################
#titles of all cd's in 1987

year = root.findall("CD")

print("All the CD's with the year '1987':")
for item in year:
    if item.find("YEAR").text == "1987":
        print(item.find("TITLE").text)
        
