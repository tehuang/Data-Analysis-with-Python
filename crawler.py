# Retrieve the HTML source code of the PPT Movie website
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

# Create a Request object with browser-like headers to avoid 403 Forbidden.
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response: 
    data=response.read().decode("utf-8") #HTML, CSS, JS

# Parse the source code to get the daily article titles
import bs4  # Beautiful Soup: parse and extract data from HTML
root = bs4.BeautifulSoup(data,"html.parser") 
#print(root.title.string) #Print out the title of the page
#titles = root.find("div",class_="title") # Find the <div> tags with class="title"
titles = root.find_all("div",class_="title") # Find all <div> tags with class="title"
for title in titles: 
    if title.a != None: # Only print titles that contain an <a> tag
        print(title.a.string)
    