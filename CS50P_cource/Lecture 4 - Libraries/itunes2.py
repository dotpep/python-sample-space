import json
import requests

name = input("Artist Name: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + name[1])
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
