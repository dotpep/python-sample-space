import json
import requests

types = input('"types": "artifacts","boss","characters","consumables",'
              '"domains","elements","enemies","materials","nations","weapons"')

name = input("name: ")
choose = input("data: ")

response = requests.get(f"https://api.genshin.dev/{types}/{name}")

results = response.json()
print(results[choose])
