from . import UseFirebase
from . import XMLManipulate

def updateArticles(): #Add all new articles to DB
    for feed in UseFirebase.getFeeds(): #For each RSS feed

        link = feed["link"] #Get the RSS link

        rawData = XMLManipulate.convertRawData(link) #Convert XML to Python-struct

        data = XMLManipulate.rawDataToDict(rawData) #Turn struct into dict

        UseFirebase.postArticles(data) #Post new articles to DB

