from . import UseFirebase
from . import XMLManipulate

def updateArticles(): #Add all new articles to DB
    for feed in UseFirebase.get_feeds(): #For each RSS feed

        link = feed["link"] #Get the RSS link

        rawData = XMLManipulate.convert_raw_data(link) #Convert XML to Python-struct

        data = XMLManipulate.raw_data_to_dict(rawData) #Turn struct into dict

        UseFirebase.post_articles(data) #Post new articles to DB

