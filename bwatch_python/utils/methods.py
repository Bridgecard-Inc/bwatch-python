from base64 import b64decode, b64encode, encode
import base64
from datetime import datetime, timedelta
from typing import Dict
import json
import uuid


def base64EncodeDict(data: Dict):

    return base64.urlsafe_b64encode(json.dumps(data).encode()).decode()


def base64DecodeToDict(encodedString: str):

    data = json.loads(base64.urlsafe_b64decode(encodedString.encode()).decode())

    return data


def getCurrentTimestamp():
    return int(datetime.timestamp(datetime.now()))


def fetch_usecase_rules(rules: dict):

    high_rules = rules

    total_list = []

    total_list.extend(list(high_rules.values()) if high_rules else [])

    return {"data": total_list}


def get_key_val(data_key, data):

    data_key_list = data_key.split(".")

    data_value = 0

    for key_index in range(len(data_key_list)):

        if key_index == 0:

            data_value = data.get(data_key_list[key_index].lstrip().rstrip())

        else:

            data_value = data_value.get(data_key_list[key_index].lstrip().rstrip())

    return data_value


def data_mapper(data: dict, mapping: dict):
    bwatch_data = {}

    for key in mapping:
        map_value_from_key = mapping[key]
        if type(map_value_from_key) == dict:
            temp_data = data_mapper(data, map_value_from_key)
            mapping[key] = temp_data
        else:

            if "." in map_value_from_key:

                mapping[key] = get_key_val(map_value_from_key, data)

            else:

                if map_value_from_key in data:
                    mapping[key] = data[map_value_from_key]

    return mapping
