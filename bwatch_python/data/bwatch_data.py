from .customer.schema.cusotmer_data import Customer
from .customer.crud.customer import crud_customer


def create_customer(data: dict, mapping: dict):
    bwatch_data = {}
    for key in mapping:
        map_value_from_key = mapping[key]
        if map_value_from_key in data:
            bwatch_data[key] = data[map_value_from_key]

    if not bwatch_data:
        return {
            "message": "incorrect mapping"
        }
    customer = Customer(**bwatch_data)
    result = crud_customer.create(obj_in=customer)

    if not result:
        return {
            "message": "failed"
        }

    return {
        "message": "success"
    }
