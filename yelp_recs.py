import requests
import json
from getpass import getpass
import os
from dotenv import load_dotenv
from pprint import pprint

CLIENT_ID = getpass("CLIENT_ID:")
API_KEY = getpass("API_KEY:")


yelp_api = "https://api.yelp.com/v3/"
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
response = requests.get(url=yelp_api, params=request_params, headers=request_headers)
parsed_response = json.loads(response.text)
pprint(parsed_response)