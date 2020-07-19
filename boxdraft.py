import requests
import os.path
import json
import glob
import sys
import time
from os import path

#URL that is used as base for API calls
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id="
#Folders that are used as a data cache and storage for original files, respectively.
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
    fullurl = url + id
    print("Full path is: " + fullpath)
    if(not(path.exists(fullpath))):
        print("Fetching new card...")
        req = requests.get(fullurl)
        f = open(fullpath, "x")
        f.write(req.text)
        f.close()
        print(req.text)
        time.sleep(0.05)
    else:
        print("File exists!")
        f = open(fullpath)
        info = json.load(f)
        print(info)
        f.close()

def parse_sets():
    idset = []
    setlist = []
    for file in glob.glob(folder2 + "*.ydk"):
        setlist.append(file)
    print(setlist)
    for file in setlist:
        f = open(file)
        while True:
            line = f.readline()
            line = line.rstrip(" \n")
            if not line:
                break
            if(line[0] >= "0" and line[0] <= "9"):
                idset.append(line)
        f.close()
    return idset


all_ids = parse_sets()
for id in all_ids:
    search_id(id)
