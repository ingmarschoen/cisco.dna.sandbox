"""get an auth token from cisco DNA sandbox via api"""
import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_HOST, DNAC_USER, DNAC_PASSWORD

def get_auth_token():
    """
    Building an http auth request. Using requests.post to make a call to the Auth API Endpoint
    """
    url = 'https://'+DNAC_HOST+'/dna/system/api/v1/auth/token' # URL of the API Endpoint
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))  # Make a POST Request to the endpoint
    token = resp.json()['Token']  # Retrieve the Token from the returned JSON of the http response
    print("Token Retrieved: {}".format(token))  # Print the Token from the response of the endpoint
    return token    # return the token back for later use

if __name__ == "__main__":
 get_auth_token()
