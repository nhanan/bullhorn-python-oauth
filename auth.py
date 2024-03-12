import requests
from urllib.parse import urlparse

# Consult BH Support to set up API user and get client id + secret
# Visit https://rest.bullhornstaffing.com/rest-services/loginInfo?username={api_user} to get URLs

api_user = API_USER
api_pass = API_PASS
client_id = CLIENT_ID
client_secret = CLIENT_SECRET
rest_url = "https://rest.bullhornstaffing.com/" # May need to change these depending on where you're based - see notes above

def start():
    return(login(str(getAccessToken())))

def get_cluster_information():
    rest_url = f"https://rest.bullhornstaffing.com/rest-services/loginInfo?username={api_user}"
    response = requests.request("POST", rest_url)
    auth_url = response.json()['oauthUrl']
    return(auth_url)

auth_url = get_cluster_information()

def getAccessToken():
    authCode = getAuthCode()
    url = f"{auth_url}/token?grant_type=authorization_code&code={authCode}&client_id={client_id}&client_secret={client_secret}"
    response = requests.request("POST", url)
    accessToken = response.json()["access_token"]
    return(accessToken)

def getAuthCode():
    url = f"{auth_url}/authorize?client_id={client_id}&response_type=code&action=Login&username={api_user}&password={api_pass}"
    response = requests.request("GET", url)
    response = urlparse(response.url)
    authCode = response[4][5:60:]
    return(authCode)

def login(accessToken):
    url = f"{rest_url}rest-services/login?version=*&access_token={accessToken}"
    response = requests.request("POST", url)
    print("Bullhorn API Login: " + response.reason)
    return(response.json()["BhRestToken"])


# Call start function to authenticate the session, then you can make API calls to your Bullhorn ATS instance
start()
