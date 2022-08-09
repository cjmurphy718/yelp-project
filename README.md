# yelp-project

## Setup

Create an API Key on the Yelp website:
https://www.yelp.com/developers/v3/manage_app
Save this in a .env file under "API_KEY" and "CLIENT_ID"

Create a virtual environment
```sh
conda create yelp-env
```

Activate your virtual environment
```sh 
conda activate yelp-env
```

Install requirements
```sh
pip install yelpapi
```

Run the code
```sh
python yelp_recs.py
```

Input your Client ID and hit enter, followed by your API Key and hit enter - You will not see the text.