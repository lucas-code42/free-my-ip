import requests

url ='http://127.0.0.1:3030/freemyip'
payload = {}
test = requests.get(url=url)
print(test.json())