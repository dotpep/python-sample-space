import requests

name = input("Your name: ")

response = requests.get("https://itunes.apple.com/ search?entity=song&limit=1&term=" + name[1])
print(response.json())
