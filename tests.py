from DataManipulation import UseFirebase, XMLManipulate

def check_article_connection(): #Make sure there are articles, and can be connected
    """ function to ensure DB connection and format """
    assert len(UseFirebase.get_articles()) > 0 #There are articles in the DB that I manually seeded to check the connection


def check_feed_connection(): #Make sure there are feeds, and can be connected
    """ function to ensure DB connection and format """

    assert len(UseFirebase.get_articles()) > 0 #There are articles in the DB that I manually seeded to check the connection

def check_raw_data_get(): #Make sure dict contains proper data
    """ function to make sure data gets properly formatted. """
    output = XMLManipulate.convert_raw_data("https://www.google.com/alerts/feeds/00698824683610429194/1098921106065488311")
    assert isinstance(output, dict) 
    assert len(output["entry"]) > 0 #Google Alerts feeds prepopulate, and given that this is a COVID feed, it should have 20 articles
    assert output["entry"][0]["title"]["#text"] #Make sure title exists
    print(output["entry"][0]["title"]["#text"]) #Make sure title is properly formatted

def check_data_formatter():
    """ function to make sure data gets properly formatted. """
    #Run function and save output
    output = XMLManipulate.raw_data_to_dict(XMLManipulate.convert_raw_data("https://www.google.com/alerts/feeds/00698824683610429194/1098921106065488311"))
    assert isinstance(output, dict) 
    assert len(output["entries"]) > 0 #Google Alerts feeds prepopulate, and given that this is a COVID feed, it should have 20 articles
    assert output["entries"][0]["title"] #Make sure title exists under proper name
    print(output["entries"][0]["title"]) #Make sure title is properly formatted
    print(output["entries"][0]["published"]) #Make sure title is a real date

def run_tests(): #GET THEM TESTS BOI
    """ function to run all tests """
    check_feed_connection()
    check_article_connection()
    check_raw_data_get()
    check_data_formatter()