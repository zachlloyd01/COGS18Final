from flask import Flask, render_template, redirect, jsonify, request
from dataManipulation import UseFirebase, ArticleData, FeedData
import datetime

app = Flask(__name__) #Lazyloading

@app.route('/') #Root domain
def home(): #Homepage
    articles = UseFirebase.getArticles() #Get articles

    articles.sort(key = lambda x:datetime.datetime.strptime(x['published'], '%Y-%m-%d'))
    return render_template('home.html', articles=articles) #Render home.html, with data

@app.route('/feeds') #Feeds List Page
def feeds():
    feeds = UseFirebase.getFeeds() #Get list of feeds

    return render_template('feeds.html', feeds=feeds) #Render the template with data

@app.route('/update', methods=['POST']) #Update articles, POST to prevent CORS attacks
def update():
    try:
        ArticleData.updateArticles() #Update articles
        return jsonify("done") #Return JSON done response
    except:
        return jsonify("error") #Error

@app.route('/addfeed') #Add new feed page
def addFeed():
    return render_template('addfeed.html') #Render the page


@app.route('/postfeed', methods=['POST']) #Add new feed to the database, POST to prevent CORS attacks
def postFeed():
    url = request.form['url'] #Get the URL inputted by the user
    FeedData.addFeed(url) #Add URL to the DB
    return redirect('/feeds') #Go back to feeds table

UseFirebase.init() #Turn on Firebase connection
app.run() #Open webserver