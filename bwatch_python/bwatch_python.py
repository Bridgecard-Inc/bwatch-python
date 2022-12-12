import sys

from .utils import db_stream

from .utils.bwatch_data_context import bwatch_python_data_context


def init(auth_data: dict, middleware_data: dict, data_mappers: dict):
    """
    Initialises Bwatch package.

    """

    app_id = auth_data.get("app_id") or ""

    bwatch_python_data_context.app_id = app_id

    bwatch_python_data_context.auth_token = auth_data.get("auth_token") or ""

    bwatch_python_data_context.high_urgency_usecase_rules_dict = {}

    bwatch_python_data_context.fraudulent_customers_dict = {}

    url_to_track_on_middleware = middleware_data.get("url_to_track_on_middleware") or ""

    id_to_track_on_middleware = middleware_data.get("id_to_track_on_middleware") or ""

    bwatch_python_data_context.url_to_track_on_middleware = url_to_track_on_middleware

    bwatch_python_data_context.id_to_track_on_middleware = id_to_track_on_middleware

    customers_data_mappers = data_mappers.get("customers") or ""

    transactions_data_mappers = data_mappers.get("transactions") or ""

    bwatch_python_data_context.customers_data_mappers = customers_data_mappers

    bwatch_python_data_context.transactions_data_mappers = transactions_data_mappers

    high_urgency_usecase_rules_dict_URL = (
        f"https://bwatch-admin-database.firebaseio.com/rules/{app_id}/HIGH"
    )
    S = db_stream.subscriber(
        high_urgency_usecase_rules_dict_URL,
        __handle_stream_high_urgency_usecase_rules_dict,
    )

    fraudulent_customers_dict_URL = (
        f"https://bwatch-admin-database.firebaseio.com/fraudulent_customers/{app_id}"
    )
    T = db_stream.subscriber(
        fraudulent_customers_dict_URL, __handle_stream_fraudulent_customers_dict
    )

    S.start()
    T.start()
    return


def __handle_stream_high_urgency_usecase_rules_dict(data: any):

    base_data = data[1]

    path = base_data.get("path")

    data = base_data.get("data")

    path_list = path.split("/")[1:]

    path_list = [item for item in path_list if item]

    # Handle item added event ('put', {'path': '/', 'data': {'-NH5enCoiQAM6uBMkAHY': {'app_id': '80406fc4-ec8a-4990-bf82-bb50dc97e721', 'created_at': 1668706676,
    # 'rule_description': 'This is a test rule', 'rule_key': 'user.data', 'rule_parameter': 'DATA_COMPARISON_EQUAL_TO', 'rule_score': 0,
    #  'rule_urgency': 'HIGH', 'rule_value': ''}, '-NH6Q7PCCWU8P1JBgoev': {'app_id': '80406fc4-ec8a-4990-bf82-bb50dc97e721', 'created_at': 1668719345,
    # 'rule_description': 'This is a test rule', 'rule_key': 'user.data', 'rule_parameter': 'DATA_COMPARISON_EQUAL_TO', 'rule_score': 0,
    # 'rule_urgency': 'HIGH', 'rule_value': ''}, '-NH6Q9QiEUOZ7p7Svh1j': {'app_id': '80406fc4-ec8a-4990-bf82-bb50dc97e721', 'created_at': 1668719357,
    #  'rule_description': 'This is a test rule', 'rule_key': 'user.data', 'rule_parameter': 'DATA_COMPARISON_EQUAL_TO', 'rule_score': 0,
    # 'rule_urgency': 'HIGH', 'rule_value': ''}}})

    if len(path_list) == 0:

        if data is not None:

            high_urgency_usecase_rules_dict = bwatch_python_data_context.high_urgency_usecase_rules_dict

            high_urgency_usecase_rules_dict.update(data)

            bwatch_python_data_context.high_urgency_usecase_rules_dict = high_urgency_usecase_rules_dict

    # Handle item deleted event ('put', {'path': '/-NH6Q9QiEUOZ7p7Svh1j', 'data': None})

    elif len(path_list) == 1:

        key = path_list[0]

        high_urgency_usecase_rules_dict = bwatch_python_data_context.high_urgency_usecase_rules_dict

        high_urgency_usecase_rules_dict.pop(key)

        bwatch_python_data_context.high_urgency_usecase_rules_dict = high_urgency_usecase_rules_dict

    # Handle item updated event ('put', {'path': '/-NH6Q7PCCWU8P1JBgoev/created_at', 'data': 1668719845})

    elif len(path_list) == 2:

        key = path_list[0]

        field = path_list[0]

        value = data

        high_urgency_usecase_rules_dict = bwatch_python_data_context.high_urgency_usecase_rules_dict

        high_urgency_usecase_rules_dict.get(key)[
            field
        ] = value

        bwatch_python_data_context.high_urgency_usecase_rules_dict = high_urgency_usecase_rules_dict

    return


def __handle_stream_fraudulent_customers_dict(data: any):

    print(data)

    base_data = data[1]

    path = base_data.get("path")

    data = base_data.get("data")

    path_list = path.split("/")[1:]

    path_list = [item for item in path_list if item]

    # Handle item added event ('put', {'path': '/', 'data': {'8yCQj00QisOTqyOikFH7hz2sDD62': True}})

    if len(path_list) == 0:

        if data is not None:

            fraudulent_customers_dict = bwatch_python_data_context.fraudulent_customers_dict

            fraudulent_customers_dict.update(data)

            bwatch_python_data_context.fraudulent_customers_dict = fraudulent_customers_dict

    return
