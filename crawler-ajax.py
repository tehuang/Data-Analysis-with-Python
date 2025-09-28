# Main Goal: Identify the website's operation pattern and find the URL that actually returns the data
# AJAX (Asynchronous JavaScript and XML): a technique to fetch data from the server
# in the background without reloading the whole webpage.
# Hence, we have to inspect the Network panel (Fetch/XHR) to find where the data we need is stored.
# Use the Preview tab to examine the response and identify the correct field names

import ssl 
# Disable SSL certificate verification (not recommended for production).
# This allows urllib to access HTTPS sites even if the SSL certificate
# is self-signed, expired, or untrusted.
ssl._create_default_https_context = ssl._create_unverified_context
# Retrieve the code of the KKDAY website
import urllib.request as req
url="https://www.kkday.com/en-us/category/ajax_get_top_products?productCategory=CATEGORY_018&destination="

# Create a Request object with browser-like headers to avoid 403 Forbidden.
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response: 
    data=response.read().decode("utf-8") #JSON


import json
data = json.loads(data) # Parse the raw JSON data into a list of dictionaries representing surnames
posts=data["data"]
for post in posts: 
    print(post["name"])