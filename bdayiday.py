import requests
import pprint
api_key = "9606880197aeaab40442f8635092fca4918bf5"
base_url = "https://api.festdays.dev/v1/holidays"
year = "2020"
month = "1"
day = "25"
headers = {"Authorization": api_key}
query= {"year": "2020"} 
endpoint = f"{base_url}"
print(endpoint)
r = requests.get(endpoint, headers=headers,params=query)

print(r.status_code)
data = r.json()
results = data['results']
