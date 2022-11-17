from pydantic import BaseModel
from enum import Enum


class PaymentMethodDataEnum(str, Enum):
    card="CARD"
    pos="POS"
    local_bank_transfer= "LOCAL BANK TRANSFER"
    international_bank_transfer = "INTERNATIONAL BANK TRANSFER"

class PaymentTypeDataEnum(str,Enum):
    traditonal="TRADITIONAL"
    crypto_transaction = "CRYPTO TRANSACTION"

class CardTypeEnum(str, Enum):
    visa="VISA"
    mastercard="MASTERCARD"
    verve="VERVE"

class CardData(BaseModel):
    card_number:str
    card_type:CardTypeEnum
    name_on_card:str

class BankingData(BaseModel):
    bank_account_number:str
    bank_name:str

class LocationData(BaseModel):
    address:str
    latitude:str
    longitude:str
    ip_address:str
    country:str
    state:str