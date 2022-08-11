import os
import json
from pprint import pprint
import requests
import random
from dotenv import load_dotenv
#from app import APP_ENV


load_dotenv()
APP_ENV = os.getenv("APP_ENV", default="development") # use "production" on a remote server
API_KEY = os.getenv("API_KEY")
ZIP_CODE = 10001
PRICE_MEDIAN = 2
RADIUS_DEFAULT = 1000
valid_choices = ("pizza", "mexican", "italian", "mexican", "sushi", "american", "asian", "thai", "indian", "mediterannean", "greek", "japanese", "noodles", "dim sum", "seafood")
conMil = 1609.34

def get_location():
    if APP_ENV=="development":
        user_zip = input("What is your 5-digit zip code? ")
    else:
        user_zip = ZIP_CODE
    return user_zip
def get_price():
    if APP_ENV=="development":
        price_limit = input("What price do you want to pay on a scale of 1-4, 4 being the most expensive? ")
    else:
        price_limit = PRICE_MEDIAN
    return price_limit
def get_radius():
    if APP_ENV=="development":
        radius_limit = input("How many miles are you willing to go? ")
        radius_limit = int(radius_limit)
        radius_limit = radius_limit * conMil
        radius_limit = int(radius_limit)
    else:
        radius_limit = RADIUS_DEFAULT
    return radius_limit   
def get_category():
    if APP_ENV=="development":
        category_choice = input("Are you craving anything? ")
    else:
        category_choice = random.choice(valid_choices)
    return category_choice    
def get_yelp_recs(user_zip, price_limit, radius_limit, category_choice):
    request_url = "https://api.yelp.com/v3/businesses/search"
    request_params = {
        'term': 'dinner', 
        'limit': 1, 
        'price': price_limit,
        'radius': radius_limit, 
        'categories': category_choice, # FYI looks like when we do a search for businesses with categories ['chinese', 'pizza'] it seems to return either chinese OR pizza. Not restaurants that are a fusion / combination of both
        'location': user_zip
    }
    request_headers = {'Authorization': f"bearer {API_KEY}"}
    response = requests.get(url=request_url, params=request_params, headers=request_headers)
    parsed = json.loads(response.text)
    #pprint(parsed)
    businesses = parsed["businesses"]
   # business_result = []
    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
       # business_result.append({
        #business_name = business["name"]
       # "Rating": business["rating"],
       # "Address": " ".join(business["location"]["display_address"]),
       # "Phone": business["phone"]
    return
if __name__ == "__main__":
    user_zip=get_location()
    price_limit=get_price()
    radius_limit=get_radius()
    category_choice=get_category()
    result = get_yelp_recs()
    #print(get_yelp_recs())


