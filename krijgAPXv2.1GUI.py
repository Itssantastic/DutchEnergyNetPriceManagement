"""
Copyright free
Sander Vielvoije
21-03-2023
Version 2.1     WITHOUT DEBUG WITH GUI

Function of program:
Get the APX of the current hour
Steps:
1. Get current time
2. Form the URL
3. send URL (get request)
4. phrase xml to json list or string
5. extract APX called TariffReturn from json
6. Print on GUI

===SOURCES=======
USE requests   https://pypi.org/project/requests/
USE JSON       https://oxylabs.io/blog/python-parse-json
USE TIMESTAMP  https://www.geeksforgeeks.org/get-current-timestamp-using-python/
USE STRFTIME   https://www.programiz.com/python-programming/datetime/strftime 
USE PySimpleGUI https://realpython.com/pysimplegui-python/ 
=================
"""

import requests
import json
from datetime import datetime;
import PySimpleGUI as sg

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
startHour = int(now.strftime("%H"))-1
if (startHour < 10):
    startHour = "0" + str(startHour)        #add 0 and make string
else:
    startHour = str(startHour)              #make string

timeStampStart = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + "T" + startHour                             #current time minus one hour to get the previous hour
timeStampEnd = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + "T" + now.strftime("%H")                      #current time

#build the URL
url = baseURL1 + timeStampStart + baseURL2 + timeStampEnd + baseURL3
# print (url)

#get the reponse json form the api
response = requests.get(url)

#========USE LIST==========
data = response.json()                  #convert to json list
print (data[0]["TariffReturn"])         #print TariffReturn
apx = (data[0]["TariffReturn"])         #save apx value
#==========================

#========USE STRING========
jsonStr = json.dumps(data)              # convert to String
y = json.loads(jsonStr)                 #load json String
# print (y[0]["TariffReturn"])            #print TariffReturn
#==========================

#=======GUI================

layout = [[sg.Text("Hudige APX prijs : "+ str(apx))], [sg.Button("OK")]]
window = sg.Window("Demo", layout)
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
#==========================




