from enum import Enum
from pydantic import BaseModel
from .base_type_schema import (
    PaymentTypeDataEnum, PaymentMethodDataEnum, LocationData, CardData, BankingData
)

class TransactionStatusDataEnum(str, Enum):

    COMPLETED = "COMPLETED"
    PENDING = "PENDING"

    
class TransactionPaymentData(BaseModel):
    payment_method: PaymentMethodDataEnum
    payment_type: PaymentTypeDataEnum
    source_payment_location: LocationData
    destination_payment_location: LocationData
    payment_card_data: CardData
    source_payment_bank: BankingData
    destination_payment_bank: BankingData


class TransactionAmountData(BaseModel):
    amount: str
    currency: str


class TransactionStatusData(BaseModel):
    status: TransactionStatusDataEnum


class TransactionDataHistory(BaseModel):
    created_at: str
    updated_at: str
    details_update_history: str


class Transaction(BaseModel):
    id: str
    transaction_payment_data: TransactionPaymentData
    transaction_amount_data: TransactionAmountData
    transaction_status_data: TransactionStatusData
    transaction_data_history: TransactionDataHistory
