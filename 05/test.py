import requests

url = 'https://svatky.adresa.info/json?date=2412'

url = 'https://svatky.adresa.info/json?date=3012'


response = requests.get(url)

print(response) # <Response [200]>
print(response.url)
data = response.json()
print(data)

{
    "MMDD": [],
    "1224": ['Eva', 'Vašek', 'Štedrý den'],
    "1225": ['Eva', 'Vašek', 'Štedrý den'],
    "1226": [],
}


"""
1. 
"""
