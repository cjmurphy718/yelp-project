
import json
import requests
import os
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


request_url = "https://api.yelp.com/v3/businesses/search"
request_params = {
    'term': 'dinner', 
    'limit': 2, 
    #'offset': 50, 
    #'price': ['1', "2"], 
    'radius': 1000, 
    'categories': ['pizza'], # FYI looks like when we do a search for businesses with categories ['chinese', 'pizza'] it seems to return either chinese OR pizza. Not restaurants that are a fusion / combination of both
    'location': 'New York'
}
request_headers = {'Authorization': f"bearer {API_KEY}"}
response = requests.get(url=request_url, params=request_params, headers=request_headers)
parsed = json.loads(response.text)

businesses = parsed["businesses"]
for business in businesses:
    print("Name:", business["name"])
    print("Rating:", business["rating"])
    print("Address:", " ".join(business["location"]["display_address"]))
    print("Phone:", business["phone"])
    print("\n")

##Import Business Reviews
Business_ID = business["id"]
reviews_url = f"https://api.yelp.com/v3/businesses/{Business_ID}/reviews"
req = requests.get(url=reviews_url, headers=request_headers)
json.loads(req.text)
pprint(req.text)