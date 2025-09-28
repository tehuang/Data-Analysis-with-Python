# Retrieve the HTML source code of the PPT Gossip website
# Unlike the previous crawler, the PPT gossip site shows an 18+ confirmation page before
# granting access. When you check the box, the site stores a cookie recording your answer.
# To crawl the site you must:
# 1. Inspect the network / cookies to see how the site records the confirmation (name, value, path, domain).
# 2. Replicate that behavior in your requests (send the same cookie or perform the same POST).
# 3. Then request the target pages using that cookie so the site treats you as age-verified.
# Note: respect the site's terms of service and legal/ethical rules when bypassing such checks.

import urllib.request as req
def getData(url):
    # Create a Request object with browser-like headers to avoid 403 Forbidden.
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        
    })
    with req.urlopen(request) as response: 
        data=response.read().decode("utf-8") #HTML, CSS, JS

    # Parse the source code to get the daily article titles
    import bs4  # Beautiful Soup: parse and extract data from HTML
    root = bs4.BeautifulSoup(data,"html.parser") 
    titles = root.find_all("div",class_="title") # Find all <div> tags with class="title"
    for title in titles: 
        if title.a != None: # Only print titles that contain an <a> tag
            print(title.a.string)

    # Retrieve the link to the previous page
    nextLink=root.find("a",string="‹ 上頁") # Find the <a> tag whose text is "< 上頁" 
    return nextLink["href"]

#Main Program: Retrieve titles from multiple pages
pageURL="https://www.ptt.cc/bbs/gossiping/index.html"
count = 0
while count <3: 
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count+=1

