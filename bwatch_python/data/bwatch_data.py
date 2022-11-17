from bwatch_python.data.customer.crud.customer import crud_customer
from bwatch_python.data.transaction.crud.transaction import crud_transaction
from bwatch_python.data.customer.schema.cusotmer_data import Customer
from bwatch_python.data.transaction.schema.transaction import Transaction
from .core.data_mapper import data_mapper


def create_customer(data: dict, mapping: dict):
    mapped_customer = data_mapper(data=data, mapping=mapping)
    customer = Customer(**mapped_customer)
    result = crud_customer.create(obj_in=customer)

    if not result:
        return {
            "message": "failed"
        }

    return {
        "message": "success"
    }

def create_transaction(data:dict,mapping:dict):
    mapped_transaction = data_mapper(data=data,mapping=mapping)

    transaction = Transaction(**mapped_transaction)
    result = crud_transaction.create(transaction)

    
    if not result:
            return {
                "message": "failed"
            }

    return {
            "message": "success"
        }
