from typing import Dict, List, Optional
from pydantic import BaseModel
from .banking_data import BankingData


class CustomerData(BaseModel):
    id:str
    first_name:str
    last_name:str
    middle_name:str
    email_address:str
    phone:str



class CustomerBankingData(BankingData):
    bank_verification_number:str

class CustomerIdentityData(BaseModel):
    image_of_valid_government_id:str
    valid_government_id_number:str
    selfie_image_of_user:str

class CustomerDataHistory(BaseModel):
    created_at:str
    updated_at:Optional[str]
    update_history:Dict
