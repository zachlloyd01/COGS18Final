import requests #Get/Post data to and from web servers
import xmltodict #Parse raw XML data from RSS Feeds

def getRawData(dataLink): #Get raw data
    return requests.get(dataLink).text #Requests returns raw XML data

def convertRawData(dataLink): #Convert raw XML to Dict
    rawData = getRawData(dataLink) #Get raw XML Data
    rawDict =  xmltodict.parse(rawData, dict_constructor=dict) #Convert to OrderedDict
    
    convertedDict = rawDict["feed"] #Root element of RSS Feed
    
    return convertedDict

def rawDataToDict(rawData): #Convert all the raw data into something usable
    finalDict = {
        "title": rawData["title"],
        "entries": []
    }
    
    for article in rawData["entry"]: #Entry is an array in the dict
        if "#text" in article["title"]:
            articleDict = { #Get necessary elements from current entry
                "title": article["title"]["#text"], 
                "link": article["link"]["@href"],
                "content": article["content"]['#text'],
                "published": article["published"]
            }
            
            finalDict["entries"].append(articleDict) #Append current entry to the data
        
    return finalDict


    