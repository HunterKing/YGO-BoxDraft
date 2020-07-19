import requests
import os.path
import json
import glob
import sys
import time
from os import path

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id="
folder = "./data/"
folder2 = "./sets/"

if(not(path.exists(folder))):
    print("Attempting to make data storage directory.")
    os.mkdir(folder)

if(not(path.exists(folder2))):
    print("Attempting to make set directory.")
    os.mkdir(folder2)

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
        f.close()

def parse_set():
    for file in glob.glob(folder2 + "*.ydk"):
        print(file)

id = -1
while(id != "0"):
    parse_set()
    id = input("Enter an ID: ")
    if(id != "0"):
        search_id(id)
