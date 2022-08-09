
import json
import requests
yelp_api = "https://api.yelp.com/v3/"


x = requests.get(yelp_api)
print(dir(x))

data = json.loads(x.text)
print(type(data))
print(data)


##Import modules (this also may have to be moved to the requirements.txt file like the prof did for in-class samples)
pip install request ##Install requests
brew install jq ##Install json
from YelpAPI import get_my_key ## this might need to be changed to the way that prof wants us to embedd the key?



## Define the API key, Define the end point, and define the header
API_KEY = get_my_key()
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearers %s' % API_KEY}

## Define parameters
PARAMETERS = {'term': 'sushi',
              'limit': 5,
              'location': 'New York'}

## Make a request to the Yelp API
response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)


## Convert the JSON string to a dictionary

business_data = response.json()
