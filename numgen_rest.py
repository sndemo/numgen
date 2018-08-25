import json
import requests
from requests.auth import HTTPBasicAuth

#API_HTTP="seldonapi.aws.s12n.tk"
API_HTTP="localhost:5000"

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
    payload = {"data":{"names":["a","b"],"tensor":{"shape":[2,2],"values":[0,0,1,1]}}}
    response = requests.post(
                "http://"+API_HTTP+"/api/v0.1/predictions",
                headers=headers,
                json=payload)
    print(response.text)

def gen_REST_request(batch,features,tensor=True):
    if tensor:
        datadef = {
            "names":features,
            "tensor":{
                    "shape":batch.shape,
                    "values":batch.ravel().tolist()
                    }
            }
    else:
        datadef = {
            "names":features,
            "ndarray":batch.tolist()
            }
        
    request = {
        "meta":{},
        "data":datadef
        }

    return request

def rest_request_without_oauth():
    #payload = {"data":{"names":["x"],"tensor":{"shape":[1,5,1],"values":[[[20],[21],[22],[23],[24]]]}}}
    payload = {"data":{"names":["x"],"ndarray":[[[20.0],[21.0],[22.0],[23.0],[24.0]]]}}
    #response = requests.post("http://"+API_HTTP+"/predict",json=payload)
    response = requests.post("http://"+API_HTTP+"/predict", data={"json":json.dumps(payload)})
    print(response.text)

rest_request_without_oauth()
