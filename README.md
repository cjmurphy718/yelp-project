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
pip install -r requirements.txt
```



## Run Web App
```sh
FLASK_APP=web_app flask run
```