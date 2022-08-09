
import json
import requests
import os
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


request_url = "https://api.yelp.com/v3/businesses/search"
request_params = {
    'term': 'breakfast', 
    'limit': 50, 
    'offset': 50, 
    'price': ['1', "2"], 
    'radius': 10000, 
    'categories': ['chinese', 'pizza'], # FYI looks like when we do a search for businesses with categories ['chinese', 'pizza'] it seems to return either chinese OR pizza. Not restaurants that are a fusion / combination of both
    'location': '20002'
}
request_headers = {'Authorization': f"bearer {API_KEY}"}
response = requests.get(url=request_url, params=request_params, headers=request_headers)
parsed_response = json.loads(response.text)
pprint(parsed_response)