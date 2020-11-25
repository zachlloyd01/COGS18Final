from . import UseFirebase
from . import XMLManipulate

def addFeed(feedURL): #Add feed to the DB
    UseFirebase.addFeed(feedURL)
