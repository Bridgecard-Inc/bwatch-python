from pydantic import BaseModel

class BankingData(BaseModel):
    bank_account_number:str
    bank_name:str