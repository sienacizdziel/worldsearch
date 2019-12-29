from flask import Flask, render_template, request, redirect
import os
import requests

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

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
        print (info["candidates"])
        dictionary = {
            "latitude": candidate["geometry"]["location"]["lat"],
            "longitude": candidate["geometry"]["location"]["lng"],
            "address": candidate["formatted_address"]
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
            news_articles.append(dictionary)
        return news_articles
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def worldsearch():

    if request.method == "POST":

        placesearch = request.form.get("input")
        map_info = map_search(placesearch)
        if map_info == None:
            return redirect("/error")
        news = news_search(map_info[0]["address"])

        return render_template("news.html", map_info=map_info, latitude=map_info[0]["latitude"], longitude=map_info[0]["longitude"], news=news)

    else:
        return render_template("worldsearch.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/error", methods=["GET", 'POST'])
def error():
    if request.method == "POST":
        return redirect("/")

    else:
        return render_template("error.html")
