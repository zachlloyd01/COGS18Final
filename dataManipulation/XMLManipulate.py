import requests #Get/Post data to and from web servers
import xmltodict #Parse raw XML data from RSS Feeds

def get_raw_data(data_link): #Get raw data
    """ function to pull raw RSS data. returns string of XML """
    return requests.get(data_link).text #Requests returns raw XML data

def convert_raw_data(data_link): #Convert raw XML to Dict
    """ function to convert raw XML into an unformatted dict. Returns dict. """
    raw_data = get_raw_data(data_link) #Get raw XML Data
    raw_dict =  xmltodict.parse(raw_data, dict_constructor=dict) #Convert to OrderedDict
    
    converted_dict = raw_dict["feed"] #Root element of RSS Feed
    
    return converted_dict

def raw_data_to_dict(raw_data): #Convert all the raw data into something usable
    """ function to create a formatted dict containing 
    an array of articles, each one is a formatted dict. Returns dict.  """
    final_dict = { 
        "title": raw_data["title"],
        "entries": [] #Add articles jere
    }
    
    for article in raw_data["entry"]: #Entry is an array in the dict
        if "#text" in article["title"] and '#text' in article['content']:
            article_dict = { #Get necessary elements from current entry
                "title": article["title"]["#text"], 
                "link": article["link"]["@href"],
                "content": article["content"]['#text'],
                "published": article["published"]
            }
            
            final_dict["entries"].append(article_dict) #Append current entry to the data
        
    return final_dict


    