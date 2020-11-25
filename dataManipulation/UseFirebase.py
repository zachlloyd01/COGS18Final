#FIREBASE Imports
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

def init(): #Initialize the database
    try:
        cred = credentials.Certificate('firebaseKey.json') #Service Account for DB Access

        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://zachfeeds-86449.firebaseio.com/' #Create FB at this URL
        })

        print("Firebase root created!")

    except: #App already exists!
        print("Firebase root already existed!")


def getArticles(): #Get all articles from the database
    ref = db.reference('articles') #get articles data

    articles = ref.get()

    storedArticles = [] #Array of stored articles to later iterate over

    if articles:
        for article in articles: #For article in FB return
            currentArticle = {} 
            for elem in articles[article]: #For each element of the article
                currentArticle[elem] = articles[article][elem] #Append data to the dict
            storedArticles.append(currentArticle) #Append the dict to the array
    
    return storedArticles

def getFeeds(): #Get all feed URLs from the database
    ref = db.reference('feeds') #Get feeds data

    feeds = ref.get()

    storedFeeds = []

    for feed in feeds:
        storedFeeds.append(
            {
                "link": feeds[feed]
            }
        )
    
    return storedFeeds

def postArticles(current_data):
    ref = db.reference('articles') #Put articles

    articles = ref.get()

    

    if articles:
        storedArticles = []

        for stored in articles:
            storedArticles.append(
                
                articles[stored]['link']
                
            )

        for article in current_data["entries"]: #For each article
        
            if not article['link'] in storedArticles:

                new_article_ref = ref.push({ #Post the data
                    'title': article['title'],
                    'link': article['link'],
                    'content': article['content'],
                    'fromFeed': article['title'],
                    'published': str(datetime.strptime(article["published"], "%Y-%m-%dT%H:%M:%SZ").date())
                })
    else:
        for article in current_data["entries"]: #For each article

            new_article_ref = ref.push({ #Post the data
                'title': article['title'],
                'link': article['link'],
                'content': article['content'],
                'fromFeed': current_data['title'],
                'published': str(datetime.strptime(article["published"], "%Y-%m-%dT%H:%M:%SZ").date())

            })
