import requests
import json
yelp_api = "https://api.yelp.com/v3/"


x = requests.get(yelp_api)
print(dir(x))

data = json.loads(x.text)
print(type(data))
print(data)