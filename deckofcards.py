# Brand new deck

import requests
import json
import pprint

url = "https://deckofcardsapi.com/api/deck/new/"

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

newDeckjson = response.json()

print(newDeckjson)

# Shuffle the deck of cards

dc = input("How many decks would you like? ")

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=" + str(dc)

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

deckJson = response.json()

id = deckJson['deck_id']

print('Your deck ID is ' + str(id))



# Draw cards

url = "https://deckofcardsapi.com/api/deck/di5y7wmjv4bf/draw/?count=2"

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print()

# Calculate each hand

# Winner/Loser

# Loop
