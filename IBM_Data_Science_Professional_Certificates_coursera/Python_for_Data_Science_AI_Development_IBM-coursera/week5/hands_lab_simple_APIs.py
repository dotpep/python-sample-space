# Example 1: RandomUser API
from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_list = r.generate_users(3)
some_list

name = r.get_full_name()
for user in some_list:
    print(user.get_full_name(), " ", user.get_email())


# Generate photos of the random 5 users.
# Exercise 1
r = RandomUser()
some_list = r.generate_users(3)
for user in some_list:
    print(user.get_picture())


# Generate Table
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



# Example 2: Fruitvice API
import requests
import json

data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)

df1 = pd.DataFrame(results)
df2 = pd.json_normalize(results)

cherry = df2.loc[df2["name"] == 'Cherry']
print((cherry.iloc[0]['family']) , (cherry.iloc[0]['genus']))


# Find out how many calories are contained in a banana
# Exercise 2

banana = df2.loc[df2["name"] == "Banana"]
print(f"{banana.iloc[0]['name']} has: {banana.iloc[0]['nutritions.calories']} calories")
