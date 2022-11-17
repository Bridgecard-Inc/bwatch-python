import json
import requests
import logging
from src.utils.http_requests_helper import http_request
from . import constants

logger = logging.getLogger(__name__)


class OneSignalHelper:
    """
    OneSignalHelper class for all the functions and methods to the OneSignal API.

    Central class that is used to interact with the OneSignal API's consumed in this
    service.

    Attributes:
        app_id: OneSignal app id
        rest_api_key: secret OneSignal rest api key

    """

    base_api = "https://onesignal.com/api/v1/"

    def __init__(self, app_id, rest_api_key):
        """Inits OneSignal with connection details"""
        self.app_id = app_id
        self.rest_api_key = rest_api_key

    def create_notification(self, notification):

        """
        Send a notification

        Attributes:
            notification: instance of a *Notification class
        Returns:
            A dict of the API response
        """

        payload = {
            "app_id": constants.ONE_SIGNAL_ANDROID_APP_ID,
            "include_player_ids": notification["one_signal_id"],
            "contents": {"en": notification["message_body"]},
            "headings": {"en": notification["message_title"]},
        }

        response = http_request(
            url=self.base_api + constants.ONE_SIGNAL_CREATE_NOTIFICATIONS_ENDPOINT,
            data=json.dumps(payload),
            type_req="post",
        )

        if response.status_code != 200:
            user_id = notification["user_id"]
            logger.error(
                f"Could not send one signal notification for user - {user_id} ",
            )
            return False

        return True
