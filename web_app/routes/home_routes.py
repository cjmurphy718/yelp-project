# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

#from app.yelp_recs import get_hourly_forecasts

home_routes = Blueprint("yelp_recs", __name__)

#@weather_routes.route("/weather/form")
#def weather_form():
#    print("WEATHER FORM...")
 #   return render_template("weather_form.html")

#@weather_routes.route("/weather/forecast", methods=["POST"])
#def weather_forecast():
 #   print("WEATHER FORECAST...")
#
 #   request_data = dict(request.form)
  #  print("FORM DATA:", request_data)
#####results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    #if results:
     #   #flash("Weather Forecast Generated Successfully!", "success")
      #  return render_template("weather_forecast.html",
       #     country_code=country_code,
        #    zip_code=zip_code,
         #   results=results
        #)
    #else:
     #   #flash("Geography Error. Please try again!", "danger")
      #  return redirect("/weather/form")

#
# API ROUTES
#

#@weather_routes.route("/api/weather/forecast.json")
#def weather_forecast_api():
#    print("WEATHER FORECAST (API)...")

#    url_params = dict(request.args)
 #   print("URL PARAMS:", url_params)

  #  country_code = url_params.get("country_code") or "US"
   # zip_code = url_params.get("zip_code") or "20057"

#    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
 #   if results:
  #      return jsonify(results)
   # else:
    #    return jsonify({"message":"Invalid Geography. Please try again."}), 404
