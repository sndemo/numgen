import json
import requests
from requests.auth import HTTPBasicAuth

API_HTTP="seldonapi.aws.s12n.tk"
#API_HTTP="localhost:5000"

def get_token():
    payload = {'grant_type': 'client_credentials'}
    response = requests.post(
                "http://"+API_HTTP+"/oauth/token",
                auth=HTTPBasicAuth('oauth-key', 'oauth-secret'),
                data=payload)
    print(response.text)
    token =  response.json()["access_token"]
    return token

def rest_request():
    token = get_token()
    headers = {'Authorization': 'Bearer '+token}
    payload = {"data":{"names":["x"],"ndarray":[[[20.0],[21.0],[22.0],[23.0],[24.0]]]}}
    response = requests.post(
                "http://"+API_HTTP+"/api/v0.1/predictions",
                headers=headers,
                json=payload)
    print(response.text)

def rest_request_without_oauth():
    payload = {"data":{"names":["x"],"ndarray":[[[20.0],[21.0],[22.0],[23.0],[24.0]]]}}
    response = requests.post("http://"+API_HTTP+"/predict", data={"json":json.dumps(payload)})
    print(response.text)

rest_request()
