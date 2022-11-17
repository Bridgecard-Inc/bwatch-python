import json
from typing import Optional
import requests

class ApiHelper():
    def __init__(self, token: str):
        self.headers =  {
                "Accept": "application/json",
                "token": f"Bearer {token}",
                "Content-Type": "application/json"
            }


    def post(self, url:str, data: dict):

        response = requests.post(url=url, headers=self.headers, data=json.dumps(data))

        
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return {}


    def delete(self, url:str):

        response = requests.delete(url=url, headers=self.headers)

        
        if response.status_code == 200:
            return True
        else:
            return False

    
    def patch(self, url:str, data: Optional[dict]={}):

        response = requests.patch(url=url, headers=self.headers,data=json.dumps(data))

        
        if response.status_code == 200:
            return True
        else:
            return False


    
