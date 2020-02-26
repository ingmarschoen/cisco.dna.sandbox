"""get a list of devices from DNA with the auth token via the api"""
import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_HOST, DNAC_USER, DNAC_PASSWORD

def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://'+DNAC_HOST+'/dna/system/api/v1/auth/token'
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD)) 
    token = resp.json()['Token']
    return token

def get_network_device_list():
    # alternative writing for querystring = {"macAddress": device_id} 
    querystring="serialNumber=FCW2136L0AK" # filter results with params, hard code serial from the sandbox
    token = get_auth_token()
    url = 'https://'+DNAC_HOST+'/api/v1/network-device'
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, headers=hdr, params=querystring)
    device_list = resp.json()
    print(device_list)

if __name__ == "__main__":
    get_network_device_list()
