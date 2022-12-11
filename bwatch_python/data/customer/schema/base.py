from pydantic import BaseModel
from typing import Dict, Optional, Any
from enum import Enum


class BaseResponseSchema(BaseModel):
    status: str
    message: str


class BaseResponseSchemaData(BaseModel):
    status: str
    message: str
    data: Dict[str, Any]

class EnvironmentEnum(str, Enum):
    sandbox = "sandbox"
    production = "production"


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
    card_id: Optional[str]
    card_number: Optional[str]
    card_type: Optional[CardTypeEnum]
    name_on_card: Optional[str]

class BankingData(BaseModel):
    bank_account_number: Optional[str]
    bank_name: Optional[str]

class LocationData(BaseModel):
    address: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    ip_address: Optional[str]
    country: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
