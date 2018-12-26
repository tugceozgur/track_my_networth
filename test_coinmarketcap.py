import requests

url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url) 
data = resp.json() # Check the JSON Response Content documentation below
print(data)
