
import json
import requests
import os
from pprint import pprint
import random
from IPython.display import Image, display
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
valid_choices = ("pizza", "mexican", "italian", "mexican", "sushi", "american", "asian", "thai", "indian", "mediterannean", "greek", "japanese", "noodles", "dim sum", "seafood")
##Get User Inputs
location = input("What is your location? ")
craving = input("Do you have a craving? (Yes/No) ")
craving = craving.upper()
if craving == "YES":
    category = input("What are you craving? ")
else:
    category = random.choice(valid_choices)
miles = input("How many miles are you willing to go? ")
miles = int(miles)
conMil = 1609.34
radius = miles * conMil
radius = int(radius)
#print(radius)
price = input("What price do you want to pay on a scale of 1-4, 4 being the most expensive? ")
if price > "4":
    print("This is not a valid option! ")
    quit()
# COME BACK TO THIS - get it to loop
request_url = "https://api.yelp.com/v3/businesses/search"
request_params = {
    'term': 'dinner', 
    'limit': 1, 
    'price': price,
    'radius': radius, 
    'categories': category, # FYI looks like when we do a search for businesses with categories ['chinese', 'pizza'] it seems to return either chinese OR pizza. Not restaurants that are a fusion / combination of both
    'location': location,
}
request_headers = {'Authorization': f"bearer {API_KEY}"}
response = requests.get(url=request_url, params=request_params, headers=request_headers)
parsed = json.loads(response.text)
#pprint(parsed)

image_url = "https://api.yelp.com/v3/businesses/{id}}"
businesses = parsed["businesses"]
for business in businesses:
    print("Name:", business["name"])
    print("Rating:", business["rating"])
    print("Address:", " ".join(business["location"]["display_address"]))
    print("Phone:", business["phone"])
    # print(business["photos"])
   # image_url = business["image_url"]
    #display(Image(url=image_url, height=100))
    #print("\n")

## Import Business Reviews
business_id = business["id"]
reviews_url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"
req = requests.get(url=reviews_url, headers=request_headers)
parsed_reviews = json.loads(req.text)

print("What have recent visitors said about", business["name"], "...")
for review in parsed_reviews["reviews"]:
    print("Rating: ", review["rating"])
    print(review["text"])
