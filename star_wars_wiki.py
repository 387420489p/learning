#-------------------------STAR WARS WIKI-----------------------------------#
#you can search anythong with the power of SWAPI!
import requests
import json

response = requests.get(f"https://swapi.dev/api/")
response = response.json()

#Choose category
print("Categories:", response.keys())
data_group = input("\nChoose a category! ").lower()
response = requests.get(f"https://swapi.dev/api/{data_group}/").json()

#List all pages
next_url = response["next"]
while next_url:
    next_page = requests.get(next_url).json()
    next_url = next_page['next']
    response["results"] += next_page["results"]

#Choose stuff in category
print("\nStuff in category:", end=" ")
#FILMS exception, because it has a title key instead of a name
if data_group == "films":
    for data in response["results"]:
        print(data["title"], end="|")
        key = "title"
else:
    for data in response["results"]:
        print(data["name"], end="|")
        key = "name"
print()
data_name = input("\nChoose from list! ")
for data in response["results"]:
    if data[key].lower() == data_name.lower():
        data_id = data["url"]
response = requests.get(data_id).json()

#Choose property
print("\nAvailable properties:", response.keys())
data_self = input("\nChoose a property! ").lower()
print(f"\n{data_name}'s {data_self}: {response[data_self]}")