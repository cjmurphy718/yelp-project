# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

# /home routes
@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

# /form routes
@home_routes.route("/yelp/form")
def about():
    print("WHERE TO TONIGHT?!...")
    return render_template("yelp_form.html")

@home_routes.route("/yelp/form")
def results():
    url_params = dict(request.args)
    return render_template("yelp_results.html")