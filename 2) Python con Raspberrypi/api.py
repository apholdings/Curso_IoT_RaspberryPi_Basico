import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(response.status_code)
print(response.json().get('abilities'))