from . import UseFirebase
from . import XMLManipulate

def add_feed(feedURL): #Add feed to the DB
    """ more human-readable location 
    to run the add-feed-to-DB function. No return.  """
    UseFirebase.add_feed(feedURL)
