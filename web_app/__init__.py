
# web_app/__init__.py

#import os
#from dotenv import load_dotenv
from flask import Flask
#from app import APP_ENV

#APP_ENV = os.getenv("APP_ENV", default="production")


from web_app.routes.home_routes import home_routes
from web_app.routes.yelp_routes import yelp_routes

#from web_app.routes.book_routes import book_routes

#load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(yelp_routes)
    #app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)