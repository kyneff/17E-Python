""" Database creation using data extracted from FCC website 

Purpose: To create a dabase and maniplate it using SQL (Structured Query Languange) commands
"""

import json     #JSON (JavaScript Object Notation) ref:https://docs.python.org/3/library/json.html
import requests
import sqlite3  # A basic database engine that stores the database in a file on your computer

startFreq = input("Enter start of frequency range in MHz, minimum 225: ")
endFreq = input("Enter end of frequency range in MHz, maximum 3700: ")
tableName = "Spectrum"

con = sqlite3.connect("databasing.db") #Automatically create and connect to the database 
cur = con.cursor()  # In the database, create a cursor, which is an object that selects data in and 
                    # operates on the database or a table (created below).

#Create the table if it doesn't exist
cur.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (id, lowerBand, upperBand, bandDesc)")

# Clear all data from the table, i.e. initialize table to receive data.  Columns will not be deleted.
cur.execute("SELECT * FROM Spectrum")
cur.execute("DELETE FROM Spectrum")

#Acquire and transform the data, prepare variables for use in the for loop
response = requests.get(f"http://data.fcc.gov/api/spectrum-view/services/advancedSearch/getSpectrumBands?frequencyFrom={startFreq}&frequencyTo={endFreq}&pageNum=1&sortColumn=lowerBand&sortOrder=asc&pageSize=1000&limit=100&format=json")
content = response.text
# Parse (divide) the data string to form a python dictionary:
contentDict = json.loads(content)
spectrumList = contentDict["SpectrumBands"]["SpectrumBand"] # access data from the dictionary.

#For each frequency range, insert the values into the table
for band in spectrumList:
    specID = band["id"]
    specLow = band["lowerBand"]
    specHigh = band["upperBand"]
    specDesc = band["bandDesc"]
    cur.execute(f"""
        INSERT INTO {tableName} (id, lowerBand, upperBand, bandDesc)
        VALUES ({specID}, {specLow}, {specHigh}, "{specDesc}");
        """)
con.commit()
con.close()
''