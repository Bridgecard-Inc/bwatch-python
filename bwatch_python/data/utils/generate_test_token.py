import requests
import json
# from src.core.setup import settings
# from firebase_admin import auth


# async def generate_test_token():
rest_api_url = (
    f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
)
payload = json.dumps(
    {
        "email": "festusowumi@gmail.com",
        "password": "10qpalzm10qpalzm",
        "returnSecureToken": True,
    }
)

r = requests.post(
    rest_api_url, params={"key": "AIzaSyBffQYFMyyrqVfWdUDQ7LoeeCoUWhbNCiM"}, data=payload
)

if "localId" in r.json():
    # return r.json()["idToken"]
    print(r.json()["idToken"])
else:
    # return False 
    print(False)
