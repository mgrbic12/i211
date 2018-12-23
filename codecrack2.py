import urllib.request

page =""

num1 = 0
num2 = 0
num3 = 0
num4 = 0

url= "http://cgi.soic.indiana.edu/~dpierz/secret_vault.cgi?"
url += "groupname=Group+14&num1=" + str(num1) + "&num2=" + str(num2) + "&num3=" + str(num3) + "&num4=" + str(num4)


print(url)

web_page = urllib.request.urlopen(url)
lines = web_page.read().decode(errors="replace")
web_page.close()





for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            for num4 in range(10):
                url= "http://cgi.soic.indiana.edu/~dpierz/secret_vault.cgi?"
                url += "groupname=Group+14&num1=" + str(num1) + "&num2=" + str(num2) + "&num3=" + str(num3) + "&num4=" + str(num4)

                web_page = urllib.request.urlopen(url)
                lines = web_page.read().decode(errors="replace")
                web_page.close()

                if "Wrong!" not in lines:
                    print(lines)
