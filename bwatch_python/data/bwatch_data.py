from bwatch_python.data.customer.schema.cusotmer_data import Customer
from bwatch_python.data.transaction.schema.transaction import Transaction
from bwatch_python.utils.api_helper import ApiHelper
from ..utils.methods import data_mapper
from ..utils.bwatch_data_context import bwatch_python_data_context

api_helper = ApiHelper(token="")


def create_customer(data: dict, mapping: dict):
    mapped_customer = data_mapper(data=data, mapping=bwatch_python_data_context.customers_data_mappers)
    customer = Customer(**mapped_customer)

    response = api_helper.post(
        url=f"https://bwatch-data-service-vbdndeke7q-uc.a.run.app/v1/bwatch_service/create-customer/{bwatch_python_data_context.app_id}",
        data=customer.dict(),
    )

    if not response:
        return {
            "message": "failed"
        }

    return {
        "message": "success"
    }


def create_transaction(data:dict,mapping:dict):
    mapped_transaction = data_mapper(data=data,mapping=bwatch_python_data_context.transactions_data_mappers)

    transaction = Transaction(**mapped_transaction)

    print(transaction)

    response = api_helper.post(
        url=f"https://bwatch-data-service-vbdndeke7q-uc.a.run.app/v1/bwatch_service/create-transaction/{bwatch_python_data_context.app_id}",
        data=transaction.dict(),
    )

    print(response)

    
    if not response:
            return {
                "message": "failed"
            }

    return {
            "message": "success"
        }
