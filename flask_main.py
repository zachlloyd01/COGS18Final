from flask import Flask, render_template, redirect, jsonify
from dataManipulation import UseFirebase, ArticleData
import datetime


app = Flask(__name__)

@app.route('/') #Root domain
def home(): #Homepage
    articles = UseFirebase.getArticles() #Get articles

    articles.sort(key = lambda x:datetime.datetime.strptime(x['published'], '%Y-%m-%d'))
    return render_template('home.html', articles=articles) #Render home.html, with data

@app.route('/feeds')
def feeds():
    feeds = UseFirebase.getFeeds()

    return render_template('feeds.html', feeds=feeds)

@app.route('/update', methods=['POST'])
def update():
    ArticleData.updateArticles()
    return jsonify("done")

UseFirebase.init()
app.run()