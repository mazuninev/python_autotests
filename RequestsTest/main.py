import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '41a25723ab81849ac1192904db647fd1'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}



body_pokemons = {
    "name": "generate",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}

body_pokemons1 = {
    "pokemon_id": "14910",
    "name": "Name2",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokeball ={
    "pokemon_id": "14910"
}

response_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_pokemons)
print(response_pokemons.text)

response_pokemons1 = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_pokemons1)
print(response_pokemons1.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball)
print(response_pokeball.text)