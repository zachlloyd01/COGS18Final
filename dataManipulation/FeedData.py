from . import UseFirebase
from . import XMLManipulate

def add_feed(feedURL): #Add feed to the DB
    UseFirebase.add_feed(feedURL)
