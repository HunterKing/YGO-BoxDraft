import requests

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
req = requests.get(url)

f = open("data.json", "w")
f.write(req.text)
f.close()
