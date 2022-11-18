from typing import Dict, Optional
from pydantic import BaseModel


class EnvironmentDetails(BaseModel):
    language: str
    version: str
    package: str
    other_details: Optional[Dict[str, str]]
    ...


class SessionProperties(BaseModel):
    method: str
    url: str
    headers: Dict[str, str]
    query_params: Optional[Dict[str, str]]
    path_params: Optional[Dict[str, str]]
    client: Dict[str, str]
    cookies: Optional[Dict[str, str]]
    body: Optional[Dict[str, str]]



