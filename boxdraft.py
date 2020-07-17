import requests
import os.path
import json
from os import path

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id="
folder = "./data/"

#if(not(path.exists("data.json"))):
#    print("json doesn't exist, fetching data...\n")
#    f = open("data.json", "w")
#    f.write(req.text)
#    f.close()

def search_id(id):
    print("Searching for item with ID: " + id)
    id = id.lstrip("0")
    filename = id + ".json"
    fullpath = folder + filename
    print("Full path is: " + fullpath)
    fullurl = url + id
    print("Full url is: " + fullurl)
    req = requests.get(fullurl)
    if(not(path.exists(fullpath))):
        print("Fetching new card...")
        f = open(fullpath, "x")
        f.write(req.text)
        f.close()
        print(req.text)
    else:
        print("File exists!")
        f = open(fullpath)
        info = json.load(f)
        print(info)
        #for i in info["data"]:

id = -1
while(id != "0"):
    id = input("Enter an ID: ")
    if(id != "0"):
        search_id(id)
