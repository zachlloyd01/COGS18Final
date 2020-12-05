#FIREBASE Imports
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

def init(): #Initialize the database
    try:
        cred = credentials.Certificate('FirebaseKey.json') #Service Account for DB Access

        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://zachfeeds-86449.firebaseio.com/' #Create FB at this URL
        })

        print("Firebase root created!")

    except: #App already exists!
        print("Firebase root already existed!")


def get_articles(): #Get all articles from the database
    ref = db.reference('articles') #get articles data

    articles = ref.get()

    stored_articles = [] #Array of stored articles to later iterate over

    if articles:
        for article in articles: #For article in FB return
            stored_article = {} 
            for elem in articles[article]: #For each element of the article
                stored_article[elem] = articles[article][elem] #Append data to the dict
            stored_articles.append(stored_article) #Append the dict to the array
    
    return stored_articles

def get_feeds(): #Get all feed URLs from the database
    ref = db.reference('feeds') #Get feeds data

    feeds = ref.get() #Get data

    stored_feeds = []

    for feed in feeds:
        stored_feeds.append(
            {
                "link": feeds[feed] #Append current link to the array
            }
        )
    
    return stored_feeds

def add_feed(feedURL): #Add feed to the DB
    ref = db.reference('feeds') #Get feeds root-level
    feeds = ref.get()
    if not feedURL in feeds: 
        ref.push(feedURL) #Ad new feed to the DB

def post_articles(current_data):
    ref = db.reference('articles') #Put articles

    articles = ref.get() #Get all articles

    if articles: #If there are articles
        stored_articles = []

        for stored in articles: #Append the article link
            stored_articles.append(   
                articles[stored]['link']  
            )

        for article in current_data["entries"]: #For each article
        
            if not article['link'] in stored_articles: #Prevent duplicate articles

                new_article_ref = ref.push({ #Post the data
                    'title': article['title'],
                    'link': article['link'],
                    'content': article['content'],
                    'fromFeed': article['title'],
                    'published': str(datetime.strptime(article["published"], "%Y-%m-%dT%H:%M:%SZ").date()) #Format ISO 8061 date into Python readable
                })
    else:
        for article in current_data["entries"]: #For each article

            new_article_ref = ref.push({ #Post the data
                'title': article['title'],
                'link': article['link'],
                'content': article['content'],
                'fromFeed': current_data['title'],
                'published': str(datetime.strptime(article["published"], "%Y-%m-%dT%H:%M:%SZ").date()) #Format ISO 8061 date into Python readable
            })
