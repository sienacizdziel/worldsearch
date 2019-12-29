from flask import Flask, render_template, request, redirect, jsonify, make_response
import os
import requests
from cs50 import SQL

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///searches.db")


def map_search(input):

    # Contact API
    api_key = "AIzaSyDJgQp7OCmdRXEh-rtGVcxP8vXdsc1OLdw"
    response = requests.get(f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={input}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={api_key}")

    # Parse response
    info = response.json()
    places = []
    if len(info["candidates"]) == 0:
        return None
    for candidate in info["candidates"]:
        dictionary = {
            "latitude": candidate["geometry"]["location"]["lat"],
            "longitude": candidate["geometry"]["location"]["lng"],
            "name": candidate["name"]
        }
        places.append(dictionary)
    return places


def map_search2(latitude, longitude):

    # Contact API
    api_key = "AIzaSyDJgQp7OCmdRXEh-rtGVcxP8vXdsc1OLdw"
    response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}")

    # Parse response
    info = response.json()
    places = []
    if len(info["results"]) == 0:
        return None
    for result in info["results"]:
        place = map_search(result["formatted_address"])
        dictionary = {
            "place": place
        }
        places.append(dictionary)
    return places


def news_search(place):

    # Contact API
    api_key = "1111438c4a664b8895916ebb98fcf317"
    response = requests.get(f"https://newsapi.org/v2/everything?q={place}&sortBy=popularity&apiKey={api_key}")

    # Parse response
    info = response.json()
    news_articles = []
    if info["status"] == "ok":
        for article in info["articles"]:
            dictionary = {
                "source": article["source"]["name"],
                "title": article["title"],
                "url": article["url"],
                "time": article["publishedAt"],
                "image": article["urlToImage"],
                "description": article["description"]
            }
            time = []
            for char in dictionary["time"]:
                if ord(char) == 84:
                    break
                time.append(char)
            dictionary["time"] = "".join(time)
            news_articles.append(dictionary)
        return news_articles
    else:
        return None


@app.route("/", methods=["GET", "POST"])
def worldsearch():

    # Updating information from POST method into database for future use
    if request.method == "POST":
        search = request.form.get("input")
        db.execute(f"UPDATE searches SET search = '{search}' WHERE id = 1;")
        return redirect("/news")

    else:
        return render_template("worldsearch.html")


@app.route("/news")
def news():

    # Using database to find the search, then sending it through functions to use APIs and parse data
    placesearch = db.execute("SELECT search FROM searches WHERE id = 1;")
    map_info = map_search(placesearch[0]["Search"])
    if map_info == None:
        return redirect("/error1")
    news = news_search(map_info[0]["name"])
    if len(news) == 0:
        return redirect("/error2")
    return render_template("news.html", name=map_info[0]["name"], latitude=map_info[0]["latitude"], longitude=map_info[0]["longitude"], news=news)


@app.route("/mapnews", methods=["GET", "POST"])
def mapnews():

    # Making data readable (jsonifying)
    if request.method == "POST":
        req = request.get_json()
        res = make_response(jsonify(req), 200)
        return res

    # Finding latitude and longitude, then using application.py functions
    else:
        a = request.args.get("latitude")
        b = request.args.get("longitude")
        search = map_search2(a, b)
        number = len(search) - 2
        if len(search) == 2:
            number = 1
        if len(search) == 3:
            number = 2
        if number < 0:
            number == 0
        if search[number]["place"] == None:
            number = len(search) - 1
        print(search)
        news = news_search(search[number]["place"][0]["name"])
        return render_template("mapnews.html", latitude=a, longitude=b, name=search[number]["place"][0]["name"], news=news)


# Rendering errors
@app.route("/error1", methods=["GET", "POST"])
def error1():
    if request.method == "POST":
        return redirect("/")

    else:
        return render_template("error1.html")


@app.route("/error2", methods=["GET", "POST"])
def error2():
    if request.method == "POST":
        return redirect("/")

    else:
        return render_template("error2.html")