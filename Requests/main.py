import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a814226c18d680dbffc14ca0c31b57f2'
HEADER = {'Content - Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "alesha@mail.ru",
    "password": "Iloveqa1111"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change_name = {
    "pokemon_id": "284020",
    "name": "New Name",
    "photo_id": 2
}
body_catch_pokemon = {
    "pokemon_id": "284018"
}

response = requests.post(url = f'{URL}/trainers/reg' , headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokemon)
print(response_catch_pokemon.text)
