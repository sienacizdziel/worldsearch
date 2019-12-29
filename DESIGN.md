Hello! WorldSearch is a site that allows you to search for the most popular news about a particular region. You can search using
a searchbar or a map (clicking on the spot you want to search). The site is run in the CS50 IDE; uses HTML, Javascript, CSS, Flask,
and SQL; and utilizes a Google Maps API and a News API (https://newsapi.org/).

The backbone of the code is application.py, using Flask. When the site first opens on worldsearch.html, worldsearch() renders the
template. Worldsearch.html contains two parts: 1) a form containing a searchbar and a submit button that
posts the information for the search back into worldsearch() to be updated to a SQL database called searches.db (later used
for the "GET" part of /news) and 2) a map, created in a <script> tag. I received help with coding for everything Google Maps related
through help pages on the Google maps API and through CS50 office hours. It displays a map centered on the coordinates of New Haven. :)
Then, it uses fetch() in Javascript to send the lat/lng coordinates to the application.py function for /mapnews.
mapnews() "POST" method takes the request, makes it readable, and returns it to the Javascript in worldsearch.html.
The site is redirected to /mapnews with the returned information (lat/lng) added to the URL so that I can request it
on the "GET" method in application.py for /mapnews.

Both the news() and mapnews() functions in application.py essentially do the same thing in their "GET" methods. mapnews() has
variables for requests of longitude and latitude. These variables are inserted into the function map_search2(lat, lng) from the
top of application.py, which parses through results from the Google Maps API to find an address of the coordinates. Then, it uses
another function map_search(place), which takes in a place and returns a latitude, longitude (both unnecessary for mapnews() but
necessary for news()), and name. The results are then run through news_search(place), another function which takes the name of a
place from map_search(place) and then returns a list of dictionaries of news information like title, source, URL, etc. All of this
is passed into the html code through render_template(). news() is the same way, except it receives its information about place
to put in the map_search(place) function through the searches.db SQL database mentioned before, then follows the same steps through
news_search(place).

Once passed into html, the news.html and mapnews.html templates use the same code. They use Javascript to make a map centered
at the latitude and longitude that was returned. They also use the name that was returned as a header and have a button to go back.
Finally, they use a for loop to iterate through every item in the news dictionary, putting down the title, source, time, description, and
image. The title and source are in a form that uses a button that redirects to the URL of the news article.

Other HTML pages are "error1.html" and "error2.html", which are both redirected to depending on the issue. They also have back
buttons (used in the "POST" method of their respective application.py functions).

Layout.html contains a background color CSS <style> tag and also links to Bootstrap and styles.css. Styles.css contains a couple
style formats for classes and IDs. Fun fact: I learned what float does and I THINK IT'S SO USEFUL (especially for my images on the
news pages)!

And that is a quick overview of the design portion of WorldSearch.

Siena Cizdziel