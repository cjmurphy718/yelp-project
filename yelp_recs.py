import requests
import json
headers = {'Authorization': 'Bearer %s' % "API_KEY"}
yelp = "https://api.yelp.com/v3"

x = requests.get(yelp)
print(x.text)
