from bwatch_python.data.customer.schema.customer_data import Customer, CardData
from bwatch_python.data.transaction.schema.transaction import Transaction
from bwatch_python.utils.api_helper import ApiHelper
from ..utils.methods import data_mapper
from ..utils.bwatch_data_context import bwatch_python_data_context

from ..utils import constants

import copy

api_helper = ApiHelper()


def create_customer(data: dict):

    data_copy = copy.deepcopy(data)

    customers_data_mappers_copy = copy.deepcopy(
        bwatch_python_data_context.transactions_data_mappers
    )

    mapped_customer = data_mapper(
        data=data_copy, mapping=customers_data_mappers_copy
    )

    customer = Customer(**mapped_customer)

    response = api_helper.post(
        url=f"{constants.BWATCH_DATA_SERVICE_BASE_URL}/v1/bwatch_service/create-customer/{bwatch_python_data_context.app_id}",
        data=customer.dict(),
    )

    if not response:
        return {"message": "failed"}

    return {"message": "success"}




def update_customer_card_data(customer_id: str, data: dict):

    card_data = CardData(**data)

    response = api_helper.patch(
        url=f"{constants.BWATCH_DATA_SERVICE_BASE_URL}/v1/bwatch_service/update-customer-card-data/{bwatch_python_data_context.app_id}/{customer_id}",
        data=card_data.dict(),
    )

    if not response:
        return {"message": "failed"}

    return {"message": "success"}



def update_customer_verification_status_to_success(customer_id: str):

    response = api_helper.patch(
        url=f"{constants.BWATCH_DATA_SERVICE_BASE_URL}/v1/bwatch_service/update-customer-verification-status-to-success/{bwatch_python_data_context.app_id}/{customer_id}",
        data={},
    )

    if not response:
        return {"message": "failed"}

    return {"message": "success"}


def create_transaction(data: dict, mapping: dict):

    data_copy = copy.deepcopy(data)

    mapping_copy = copy.deepcopy(mapping)

    mapped_transaction = data_mapper(
        data=data_copy, mapping=mapping_copy
    )

    transaction = Transaction(**mapped_transaction)

    response = api_helper.post(
        url=f"{constants.BWATCH_DATA_SERVICE_BASE_URL}/v1/bwatch_service/create-transaction/{bwatch_python_data_context.app_id}",
        data=transaction.dict(),
    )

    if not response:
        return {"message": "failed"}

    return {"message": "success"}
