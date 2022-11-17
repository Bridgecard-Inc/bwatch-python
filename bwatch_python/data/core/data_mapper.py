from .error import InvalidRequest


def data_mapper(data: dict, mapping: dict):
    bwatch_data = {}
    for key in mapping:
        map_value_from_key = mapping[key]
        if map_value_from_key in data:
            bwatch_data[key] = data[map_value_from_key]
    if not bwatch_data:
        raise InvalidRequest
    return bwatch_data
