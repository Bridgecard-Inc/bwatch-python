from src.core.error import InvalidToken
import logging


logger = logging.getLogger(__name__)

PREFIX = "Bearer"


def parse_auth_token_from_header(header: str):
    if header is None:
        raise InvalidToken
    if not header.startswith(PREFIX):
        logger.error("Invalid Authentication Token")
        raise InvalidToken

    return header[len(PREFIX) :].lstrip()
