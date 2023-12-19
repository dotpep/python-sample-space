import requests
import pandas as pd
import json

"""
data = requests.get(url)
characters_payload = {"characters": "Ayaka"}
test_char = requests.get(url, params=characters_payload)
data.text
"""

"""
url = f"https://api.genshin.dev/{choose_types}/"


print(requests.get(url).text)
choose_types = input("Please choose Types as follow: ")

url1 = url + choose_types
type1 = requests.get(url1)

print(type1.text)
choose_types2 = input("Please choose Second Types as follow: ")

url2 = url + choose_types + choose_types2
type2 = requests.get(url2)

print(type2.text)
"""

def find_type2():
    type1 = input("Please choose Types as follow: ")
    type2 = input("Please choose Second Types as follow: ")


    url = f"https://api.genshin.dev/{type1}/{type2}"
    data = requests.get(url)

    print(data.text)


def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({
            "Name": user.get_full_name(),
            "Gender": user.get_gender(),
            "City": user.get_city(),
            "State": user.get_state(),
            "Email": user.get_email(),
            "DOB": user.get_dob(),
            "Picture": user.get_picture()
        })

    return pd.DataFrame(users)

df1 = pd.DataFrame(get_users())
df1


"""
data2 = requests.get("https://api.genshin.dev")
results2 = json.loads(data2.text)

df3 = pd.json_normalize(results2)
df3

"""

