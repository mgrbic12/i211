import urllib.request
import os

##web_page = urllib.request.urlopen("http://www.soic.indiana.edu/")
##contents = web_page.read().decode(errors = "replace")
##web_page.close()
##
##file_out = open("page.html", "w", encoding = "utf-8")
##file_out.write(contents)
##file_out.close()
##
##print("All done! Open page.html in your browser!")
#####################################################################
def getContent(url):
    print("Attempting to access the page at this URL:", url)
    web_page = urllib.request.urlopen(url)
    contents = web_page.read().decode(errors = "replace")
    web_page.close()

    file_name = os.path.basename(url)
    
    if file_name == "":
        file_name = "index.html"
        
    file_out = open(file_name, "w", encoding = "utf-8")
    file_out.write(contents)
    file_out.close()
   
    print("All done! Open", file_name, "in your browser\n")
    
#main
##getContent("http://cgi.soic.indiana.edu/~dpierz/I211/I211Test.html")
##getContent("http://cnn.com/")
getContent("https://www.sice.indiana.edu/")
########################################################################

    

    
