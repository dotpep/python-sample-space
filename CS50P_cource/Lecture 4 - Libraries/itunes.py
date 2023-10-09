"""import requests

name = input("Your name: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + name[1])
print(response.json())
"""

def origin():
    import requests
    import sys

    if len(sys.argv) != 2:
        sys.exit()

    response2 = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
    print(response2.json())

    """o = response2.json()
    for result in o["results"]:
        print(result["trackName"])"""

origin()
