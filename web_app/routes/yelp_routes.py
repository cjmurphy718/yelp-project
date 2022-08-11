# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.yelp_recs import get_yelp_recs

yelp_routes = Blueprint("yelp_routes", __name__)

@yelp_routes.route("/yelp/form")
def yelp_form():
    print("YELP FORM...")
    return render_template("yelp_form.html")

@yelp_routes.route("/yelp/results", methods=["POST"])
def yelp_results():
    print("YOUR DINNER PLANS...")

    request_data = dict(request.form)
    print("FORM DATA:", request_data)


    user_zip = request_data.get("user_zip") or "10001"
    print(user_zip)
    price_limit = request_data.get("price_limit") or "2"
    radius_limit = request_data.get("radius_limit") or "2"
    category_choice = request_data.get("category_choice") or "pizza"

    #zip_code = request_data.get("zip_code") or "20057"

    results = get_yelp_recs(user_zip=user_zip, price_limit=price_limit, radius_limit=radius_limit, category_choice=category_choice)
    print(results)
    if results:
        #flash("Yelp Results Generated Successfully!", "success")
        return render_template("yelp_results.html",
            user_zip=user_zip,
            price_limit=price_limit,
            radius_limit=radius_limit,
            category_choice=category_choice,
           #country_code=country_code,
            #zip_code=zip_code,
            results=results
        )
    else:
        #flash("Yelp Error. Please try again!", "danger")
        return redirect("/yelp/form")

#
# API ROUTES
#

@yelp_routes.route("/api/yelp/results.json")
def yelp_results_api():
    print("YELP RESULTS (API)...")

    url_params = dict(request.args)
    print("URL PARAMS:", url_params)

    user_zip = url_params.get("user_zip") or "10001"
    category_choice = url_params.get("category_choice") or "pizza"
    price_limit = url_params.get("price_limit") or "2"
    radius_limit = url_params.get("radius_limit") or "2"

   #ountry_code = url_params.get("country_code") or "US"
   # zip_code = url_params.get("zip_code") or "20057"

    results = get_yelp_recs(user_zip=user_zip, price_limit=price_limit, radius_limit=radius_limit, category_choice=category_choice)
    if results:
        return jsonify(results)
       # return render_template("yelp_results.html",
        #user_zip=user_zip,
         #   price_limit=price_limit,
          #  radius_limit=radius_limit,
           # category_choice=category_choice,
           #country_code=country_code,
            #zip_code=zip_code,
         #   results=results
      #  )
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404
