
import getToken
import requests

token = getToken.getRefereshToke()
print("getToken: ", token)

url = "https://app.dtuip.com/api/user/getUserInfo"
 
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token,
    "tlinkAppId": "721832e2e7bd42cfa6825995797cf656",
    "cache-control": "no-cache"
    }

 
data = {
    "userId": "73766",
    }
 
response = requests.get(url, headers=headers, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())