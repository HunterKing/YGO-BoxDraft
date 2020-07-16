import requests
import os.path
import json
from os import path

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id="
path = "./data/"
req = requests.get(url)

#if(not(path.exists("data.json"))):
#    print("json doesn't exist, fetching data...\n")
#    f = open("data.json", "w")
#    f.write(req.text)
#    f.close()

def search_id(id):
    print("Searching for item with ID: " + id)
    filename = id + ".json"
    fullpath = path + filename
    print("Full path is: " + fullpath)
    fullurl = url + id
    print("Full url is: " + fullurl)
    #f = open(fullpath, "x")
    #f.write(req.text)
    #f.close()
    print(req.text)

id = -1
while(id != 0):
    id = input("Enter an ID: ")
    if(id != 0):
        search_id(id)
