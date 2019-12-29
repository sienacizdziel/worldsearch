WorldSearch User's Manual:

Welcome to WorldSearch! The project is hosted in the CS50 IDE in the folder project/worldsearch. If you use ls, you should see, among
other things, application.py, searches.db, static/, and templates/. To begin, run "flask run" on the terminal while in the correct folder.
Once you click on the link, you will be sent to https://c9294eea-3d30-4e67-bb52-dc9f0a6a4df8-ide.cs50.xyz:8080/?.

This site is the homepage for WorldSearch. WorldSearch is a site where you can search for general news about any state, region,
or country in the world. There are two paths you can go down: 1) search for any place you have in mind in the searchbar or
2) zoom in/out of the map and click on the place you'd like to search.

Once you search for your place through either of the methods, you'll be taken to a new site, where you will see the most popular news for
that region. The site is not perfect- please keep in mind that the News API I am using will return any news article that has any
mention of the region, so some things may not seem entirely relevant. However, for the most part, you should see articles that relate
to what you searched for. At the very top in large font, you will see the keywords the News API is searching with (sometimes
they may change depending on how specific your search was). If your search was too specific or didn't make sense to the Maps/News APIs,
you'll get an error.

The news is taken from various sources. You can see the source after the article title. Below the link you'll see a date and description.
Beside those, you'll see a photo relating to the news. If you want to learn more, just click on the button, and you'll be taken to the
article.

If you'd like to return to the homepage, just click the back button.

The purpose of the site is to promote news searches of different news sources (to avoid staying in your own news/politics bubble!) and
also to make it easier to search for news general to a region through both a search bar and a map. Hope you enjoy!

Siena Cizdziel