from typing import Dict, Any, Union

import requests
from requests.models import Response


def http_request(
    url: str,
    headers: Dict[str, Any] = None,
    data: Dict[str, Any] = None,
    _json: Union[Dict[str, Any], Any] = None,
    params: Dict[str, Any] = None,
    type_req="get",
) -> Response:

    """
    Helps in making http requests

    Args:
        url (str): the url of the service
        token (str, optional): The authentication token
        data (Dict[str, Any], optional): The data to be sent
        type_req (str, optional): the type of request. Defaults to "get".
    Returns:
        Response: The response from the request
    """

    if type_req == "get":
        res = requests.get(url=url, headers=headers)
    elif type_req == "post":
        res = requests.post(url=url, data=data, headers=headers)
    elif type_req == "put":
        res = requests.put(url=url, data=data, headers=headers)
    else:
        res = requests.delete(url=url, data=data, headers=headers)
    return res
