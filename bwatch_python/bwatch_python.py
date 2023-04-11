import sys

from .database.redis import CustomRedisHandler

from .utils import db_stream

from .utils.bwatch_data_context import bwatch_python_data_context


def init(auth_data: dict, middleware_data: dict, data_mappers: dict):
    """
    Initialises Bwatch package.

    """

    app_id = auth_data.get("app_id") or ""

    bwatch_python_data_context.app_id = app_id

    bwatch_python_data_context.auth_token = auth_data.get("auth_token") or ""

    bwatch_python_data_context.secret_key = auth_data.get("secret_key") or ""

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
    
    return
