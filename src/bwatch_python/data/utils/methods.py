from base64 import b64decode, b64encode, encode
import base64
from datetime import datetime, timedelta
from typing import Dict
from AesEverywhere import aes256
import json
import uuid
from src.database.db import root_db

from src.core.config import settings


def encryptData(data: Dict):

    data = json.dumps(data)
    encryption = aes256.encrypt(data, settings.SECRET_KEY)
    encoded = b64encode(encryption).decode("utf-8")

    return encoded 

def decryptData(encoded: str):
    
    encrypted = b64decode(encoded)
    message = aes256.decrypt(encrypted, settings.SECRET_KEY)
    message = message.decode("utf-8") 
    message = json.loads(message)

    return message 

def base64EncodeDict(data : Dict):

    return base64.urlsafe_b64encode(json.dumps(data).encode()).decode()


def base64DecodeToDict(encodedString : str) :

    data = json.loads(base64.urlsafe_b64decode(encodedString.encode()).decode())

    return data

def getCurrentTimestamp():
    return int(datetime.timestamp(datetime.now()))


def generateTeamInviteLink(company_name: str, invitee_email:str, invitee_team_id:str, invite_expiry_timestamp: str):

    try:

        invite_data = {
            "invitee_email" : invitee_email,
            "invitee_team_id" : invitee_team_id,
            "role": "member",
            "invite_expiry_timestamp": invite_expiry_timestamp
        }

        encrypted_invite_data = encryptData(data=invite_data)

        team_invite_data = {
            "company_name" : company_name,
            "invite_data" : encrypted_invite_data,
        }

        encoded_team_invite_data = base64EncodeDict(team_invite_data)

        company_name_formatted =  "-".join(company_name.split(" ")) or "-"

        return f"https://bridgecard.co/{company_name_formatted}/invite/{encoded_team_invite_data}"


    except:
        return None


def decodeTeamInviteLink(invite_link: str):

    decoded_team_invite_data = base64DecodeToDict(invite_link)

    invite_data = decryptData(decoded_team_invite_data.get("invite_data") or "")

    return invite_data



def getTimestamp(year,month,day):
    return int(datetime(year,month,day).timestamp())

def getTimestampAfterDaysFromNow(days):

    current_date = datetime.today()

    result = current_date + timedelta(days=days)
    return int(result.timestamp())


def generateIssuingAppId():
    return str(uuid.uuid4())


def sortMonthList(data):

    sorted_dict = {}

    months_list = [
        "Jan",
        "Feb", 
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
        ]

    for month in months_list:

        current_year = datetime.now().year

        if f"{month}_{current_year}" in list(data.keys()):

            sorted_dict[f"{month}_{current_year}"] = data[f"{month}_{current_year}"]

    return sorted_dict


def updateBridgecardFxSwap(amount: int):
    return root_db.child("fx_swap_production_revenue").transaction(lambda current_balance: int(amount) if current_balance == None else current_balance + int(amount))