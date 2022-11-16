from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class CustomerData(BaseModel):
    id: str
    first_name: str
    last_name: str
    middle_name: str
    email_address: str
    phone: str


class CustomerBankingData(BaseModel):
    bank_verification_number: str
    bank_account_number: str
    bank_name: str


class CustomerIdentityData(BaseModel):
    image_of_valid_government_id: str
    valid_government_id_number: str
    selfie_image_of_user: str


class CustomerDataHistory(BaseModel):
    created_at: str
    updated_at: Optional[str]
    update_history: Dict[str:Any]


class Customer(BaseModel):
    customer_data: CustomerData
    customer_banking_data: CustomerBankingData
    customer_identity_data: CustomerIdentityData
    customer_data_history: CustomerDataHistory
