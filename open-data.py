
import ssl 
# Disable SSL certificate verification (not recommended for production).
# This allows urllib to access HTTPS sites even if the SSL certificate
# is self-signed, expired, or untrusted.
ssl._create_default_https_context = ssl._create_unverified_context

# import urllib.request as request
# # Open the webpagee using urllib
# # and read the HTML content from the HTTPS response.
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response: 
#     data=response.read().decode("utf-8") #HTML, CSS, JS
# # Print the raw HTML content of the page
# print(data)

# Connect to the open data API and retrieve JSON response
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
# Open the URL and directly parse the response as JSON
with request.urlopen(src) as response: 
    data=json.load(response) # 'data' is now a Python dictionary containing the JSON structure

clist=data["result"]["results"] # Access the "results" list inside the "result" field of the JSON
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")