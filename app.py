from flask import Flask, request
from proxy import FreeMyIp
import json


app = Flask('Free-my-ip')
proxy = FreeMyIp()
proxies = proxy.get_random_proxies()

@app.route('/', methods=['GET'])
def hello_world():
    respose = {
        'Message': 'Getting information from the internet is like taking a drink from a hydrant. "Mitchell Kapor".',
        'ProxyDelivery': 'Send me a HTTP GET in /freemyip and i will provide you thousands of server proxies'
    }
    return respose

@app.route('/freemyip', methods=['GET'])
def proxies_delivery():
    response = json.dumps({
        'Data': proxies
    }, indent=4)
    return response

if __name__ == "__main__":
    app.run(port=3030)