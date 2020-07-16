import requests

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
req = requests.get(url)
print(req.text)
