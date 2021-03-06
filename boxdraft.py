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
    print("Searching for item with ID: ")
    print(id)
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
        #TODO: Find a better data structure to use for this than a plain list.
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
                exists = False
                #TODO: Find a better data structure to use for this than a plain list.
                for i in idset:
                    if line in i:
                        newitem = (line, i[1] + 1)
                        idset.remove(i)
                        idset.append(newitem)               
                        exists = True
                        break
                if(not exists):
                    item = (line, 1)
                    idset.append(item)
        f.close()
    return idset


all_ids = parse_sets()
for id in all_ids:
    print(id)
    #search_id(id[0])
