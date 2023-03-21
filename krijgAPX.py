"""
Copyright free
Sander Vielvoije
21-03-2023
Version 1.0     WITH DEBUG

Function of program:
Get the APX of the current hour
Steps:
1. Get current time
2. Form the URL
3. send URL (get request)
4. phrase xml to json list or string
5. extract APX called TariffReturn from json

===SOURCES=======
USE requests   https://pypi.org/project/requests/
USE JSON       https://oxylabs.io/blog/python-parse-json
USE TIMESTAMP  https://www.geeksforgeeks.org/get-current-timestamp-using-python/
USE STRFTIME   https://www.programiz.com/python-programming/datetime/strftime 
=================
"""

import requests
import json
from datetime import datetime;

#Get current time
now = datetime.now() # current date and time

#url of mijn.easyenergy for the APX prices
url = "https://mijn.easyenergy.com/nl/api/tariff/getapxtariffs?startTimestamp=2023-03-21T18%3A00%3A00.000Z&endTimestamp=2023-03-21T19%3A00%3A00.000Z&grouping="

baseURL1        =   "https://mijn.easyenergy.com/nl/api/tariff/getapxtariffs?startTimestamp="       #First part of URL
baseURL2        =   "%3A00%3A00.000Z&endTimestamp="                                                 #Seccond part of URL
baseURL3        =   "%3A00%3A00.000Z&grouping="                                                     #Third part of URL
timeStampStart  =   "2023-03-21T18"                                                                 #Will be overrided by current time
timeStampEnd    =   "2023-03-21T19"                                                                 #Will be overrided by current time

#Get current time
timeStampStart = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + "T" + str(int(now.strftime("%H"))-1)        #minus one to select the current hour
timeStampEnd = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + "T" + str(int(now.strftime("%H"))+0)          #minus one to only select the current hour

url = baseURL1 + timeStampStart + baseURL2 + timeStampEnd + baseURL3        #build the URL
# print(url)  #Debug

#get the reponse json form the api
response = requests.get(url)
# print(response.status_code)           #debug

#========USE LIST==========

data = response.json()                  #convert to json list
# print(data)                             #print full json list    
# print(type(data))                       #debug
print (data[0]["TariffReturn"])         #print TariffReturn

#==========================


#========USE STRING========

jsonStr = json.dumps(data)              # convert to String
# print(jsonStr)                        #debug
# print(type(jsonStr))                  #debug
y = json.loads(jsonStr)
# print (y)                             #debug
# print (type(y))                       #debug

# print (y[0])                            #print full json String
# print (y[0]["TariffReturn"])            #print TariffReturn

#==========================




