import requests
import json

def getRefereshToken(): 
    url = "https://app.dtuip.com/oauth/token"
    
    headers = {"authorization": "Basic NzIxODMyZTJlN2JkNDJjZmE2ODI1OTk1Nzk3Y2Y2NTY6ODgzOTA1YjVkM2IwNGE2YWJmYzg1MDM5MGYwNDkzODM="}
    
    data = {
        "grant_type": 'password',
        "username": "18279580792",
        "password": "liu12345678",
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    #print("Status Code", response.status_code)
    #print("JSON Response ", response.json())
    if response.status_code == 200:
        return response.json()['refresh_token']
    else:
        return  ""