from . import UseFirebase
from . import XMLManipulate

def updateArticles():
    for feed in UseFirebase.getFeeds():
        link = feed["link"]

        rawData = XMLManipulate.convertRawData(link)

        data = XMLManipulate.rawDataToDict(rawData)

        UseFirebase.postArticles(data)