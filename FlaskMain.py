from flask import Flask, render_template, redirect, jsonify, request
from DataManipulation import UseFirebase, ArticleData, FeedData
import tests
import datetime

app = Flask(__name__) #Lazyloading

@app.route('/') #Root domain
def home(): #Homepage
    """ function to return home.html """
    articles = UseFirebase.get_articles() #Get articles

    articles.sort(key = lambda x:datetime.datetime.strptime(x['published'], '%Y-%m-%d'))
    articles.reverse()
    for article in articles:
        article['published'] = datetime.datetime.strptime(article['published'], '%Y-%m-%d').strftime('%m/%d/%y')
    
    return render_template('home.html', articles=articles) #Render home.html, with data

@app.route('/feeds') #Feeds List Page
def feeds():
    """ function to return feeds.html """
    feeds = UseFirebase.get_feeds() #Get list of feeds

    return render_template('feeds.html', feeds=feeds) #Render the template with data

@app.route('/update', methods=['POST']) #Update articles, POST to prevent CORS attacks
def update():
    """ POST-only function to update DB. Returns JSON """
    try:
        ArticleData.updateArticles() #Update articles
        return jsonify("done") #Return JSON done response
    except Exception as e:
        return jsonify(str(e)) #Return error to the UI


@app.route('/addfeed') #Add new feed page
def add_feed():
    """ function to render addfeed.html"""
    return render_template('addfeed.html') #Render the page


@app.route('/postfeed', methods=['POST']) #Add new feed to the database, POST to prevent CORS attacks
def post_feed():
    """ function to add feed to the DB. Returns a browser redirect. """
    url = request.form['url'] #Get the URL inputted by the user
    FeedData.add_feed(url) #Add URL to the DB
    return redirect('/feeds') #Go back to feeds table


UseFirebase.init() #Turn on Firebase connection

### UNCOMMENT THE FOLLOWING LINE TO RUN TESTS
tests.run_tests()

app.run() #Open webserver