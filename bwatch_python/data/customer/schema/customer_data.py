from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from pydantic import BaseModel
from .base import (LocationData, CardData
                               )


class CustomerStatusDataEnum(str, Enum):

    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    INACTIVE = "INACTIVE"


class CustomerData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    email_address: Optional[str]
    phone: Optional[str]
    address: Optional[LocationData]


class CustomerBankingData(BaseModel):
    bank_verification_number: Optional[str]
    bank_account_number: Optional[str]
    bank_name: Optional[str]


class CustomerIdentityData(BaseModel):
    image_of_valid_government_id: Optional[str]
    valid_government_id_number: Optional[str]
    selfie_image_of_user: Optional[str]


class CustomerDataHistory(BaseModel):
    created_at: str
    updated_at: Optional[str]
    update_history: Optional[Dict]


class CustomerStatusData(BaseModel):
    status: Optional[CustomerStatusDataEnum]


class Customer(BaseModel):
    id: Optional[str]
    issuing_company_id: Optional[str]
    customer_data: Optional[CustomerData]
    customer_card_data: Optional[List[CardData]]
    customer_banking_data: Optional[CustomerBankingData]
    customer_identity_data: Optional[CustomerIdentityData]
    customer_data_history: Optional[CustomerDataHistory]
    customer_status_data: Optional[CustomerStatusData]