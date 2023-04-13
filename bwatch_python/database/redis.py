import json
import redis

from ..utils.constants import REDIS_DB_URL, REDIS_PORT


class CustomRedisHandler():
    def __init__(self, username: str, password: str):

        password = "Bwatch-00@"+ password[:118]

        # print(username, password)

        redis_client = redis.Redis(
            host=REDIS_DB_URL,
            port=REDIS_PORT,
            username=username,
            password=password)

        self.redis_client = redis_client

        self.app_id = username

    
    def fetch_high_urgency_usecase_rules_dict(self):

        data = json.loads(self.redis_client.get(self.app_id) or '{"HIGH": {}}')
        
        if not data:

            return {}

        else:

            return data.get("HIGH")  or {}

    def fetch_fraudulent_customers_dict(self):

        data = json.loads(self.redis_client.get(self.app_id) or '{"FRAUDULENT_CUSTOMERS": {}}')
        
        if not data:

            return {}

        else:

            return data.get("FRAUDULENT_CUSTOMERS") or {}



