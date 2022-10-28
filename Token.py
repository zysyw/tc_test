
import requests

class Token:
    def __init__(self):
        self.accessToken = ""
        self.refreshToken = ""
        self.url = "https://app.dtuip.com/oauth/token"
        self.headers = {"authorization": "Basic NzIxODMyZTJlN2JkNDJjZmE2ODI1OTk1Nzk3Y2Y2NTY6ODgzOTA1YjVkM2IwNGE2YWJmYzg1MDM5MGYwNDkzODM="}
        
        self.accesstoken_data = {
            "grant_type": 'password',
            "username": "18279580792",
            "password": "liu12345678",
        }
        self.refreshtoken_data = {
        "grant_type": "refresh_token",
        "refresh_token": self.refreshToken,
        "client_id": "721832e2e7bd42cfa6825995797cf656",
        "client_secret":"883905b5d3b04a6abfc850390f049383" 
        }

    def getToken(self):

        response = requests.post(self.url, data=self.refreshtoken_data)

        #print("Status Code", response.status_code)
        #print("JSON Response ", response.json())

        if response.status_code == 200:
            rj = response.json()
            return rj['access_token']
        else:
            self.accessToken, self.refreshToken = self._getAccessToken() 
            return self.accessToken
        
    def _getAccessToken(self): 
        
        response = requests.post(self.url, headers=self.headers, data=self.accesstoken_data)
        
        #print("Status Code", response.status_code)
        #print("JSON Response ", response.json())
        if response.status_code == 200:
            return response.json()['access_token'], response.json()['refresh_token']
        else:
            return  "", ""