import os
import json
from pprint import pprint
from tkinter import N
import requests
import random
from dotenv import load_dotenv
#from app import APP_ENV


load_dotenv()
APP_ENV = os.getenv("APP_ENV", default="development") # use "production" on a remote server
API_KEY = os.getenv("API_KEY")
#API_KEY = "3WOmkQBoYZN93FxNoFjA-s-39rEC6EzX7gey0LIQaSBQhAhTp-tSNbTvoh6TR_Rwrl2NoFt1GSPuGAU32BG8-rLrnLvHQIG7kow8ABa0UuFGd6D44RcuY8Ql9F_tYnYx"
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

print("-----------\n")


def get_yelp_recs(user_zip, price_limit, radius_limit, category_choice):
#def get_yelp_recs(location, price, radius, category)
    request_url = "https://api.yelp.com/v3/businesses/search"
    request_params = {
        'term': 'dinner',
        'limit': 1,
        'price': price_limit,
        'radius': radius_limit,
        'categories': category_choice, # FYI looks like when we do a search for businesses with categories ['chinese', 'pizza'] it seems to return either chinese OR pizza. Not restaurants that are a fusion / combination of both
        'location': user_zip
    }
   # print(request_params)
    request_headers = {'Authorization': f"bearer {API_KEY}"}
    #print(request_headers)
    response = requests.get(url=request_url, params=request_params, headers=request_headers)
   # print(response)
    parsed = json.loads(response.text)
   # pprint(parsed)
    businesses = parsed["businesses"]
   # business_result = []
    for business in businesses:
        print("-----------\n")
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
       # business_result.append({
        #business_name = business["name"]
       # "Rating": business["rating"],
       # "Address": " ".join(business["location"]["display_address"]),
       # "Phone": business["phone"]
        ## Import Business Reviews
    business_id = business["id"]
    reviews_url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"
    req = requests.get(url=reviews_url, headers=request_headers)
    parsed_reviews = json.loads(req.text)
    print("-----------\n")
    print("What have recent visitors said about", business["name"], "...")
    for review in parsed_reviews["reviews"]:
        print("Rating: ", review["rating"])
        print(review["text"])
    return businesses, parsed_reviews
if __name__ == "__main__":
    user_zip=get_location()
    price_limit=get_price()
    radius_limit=get_radius()
    category_choice=get_category()
    business,parsed_reviews = get_yelp_recs(user_zip, price_limit, radius_limit, category_choice)
    #print(get_yelp_recs())
