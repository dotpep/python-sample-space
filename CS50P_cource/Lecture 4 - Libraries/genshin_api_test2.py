import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://genshin-db-api.vercel.app/api/characters?query=" + sys.argv[1])

results = response.json()
print(results["birthday"])
