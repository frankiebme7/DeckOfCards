import requests
import json
import pprint

# Start game

answer = input("Are you ready to play a new game of BlackJack? (yes/no)")

if answer == "yes":
    print("Great, let's continue. ")
else:
    print("OK, let's stop here. ")

# Shuffle the deck of cards

dc = input("How many decks would you like? ")

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=" + str(dc)

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

deckJson = response.json()

newid = deckJson['deck_id']

print('Your deck ID is ' + str(newid))

# Draw cards
draw = input("Draw? (yes/no) ")

if draw == "yes":
    print("Here's your cards! ")
else:
    print("Ok, your locked in! ")

url = "https://deckofcardsapi.com/api/deck/di5y7wmjv4bf/draw/?count=2"

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Calculate each hand

# Winner/Loser

# Loop
