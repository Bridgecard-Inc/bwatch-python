from typing import Any, Dict, Optional
from pydantic import BaseModel
from enum import Enum


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
    body: Optional[Dict[str, Any]]


class RuleParameterEnum(str, Enum):

    DATA_COMPARISON_EQUAL_TO = "DATA_COMPARISON_EQUAL_TO"
    DATA_COMPARISON_NOT_EQUAL_TO = "DATA_COMPARISON_NOT_EQUAL_TO"
    DATA_MATCH_GREATER_THAN = "DATA_MATCH_GREATER_THAN"
    DATA_MATCH_LESS_THAN = "DATA_MATCH_LESS_THAN"
    DATA_COMPARISON_EXISTS_IN = "DATA_MATCH_EXISTS_IN"
    DATA_COMPARISON_EXISTS_NOT_IN = "DATA_MATCH_EXISTS_NOT_IN"
    DATA_VELOCITY = "DATA_VELOCITY"


class RuleUrgencyEnum(str, Enum):

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class Rule(BaseModel):
    app_id: str
    created_at: int
    key: str
    description: str
    parameter: RuleParameterEnum
    value: Any
    urgency: RuleUrgencyEnum
    risk_score: int
