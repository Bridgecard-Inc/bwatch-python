from pydantic import BaseModel
from typing import Dict, Optional, Any
from enum import Enum


class BaseResponseSchema(BaseModel):
    status: str
    message: str


class BaseResponseSchemaData(BaseModel):
    status: str
    message: str
    data: Dict[str, Any]

class EnvironmentEnum(str, Enum):
    sandbox = "sandbox"
    production = "production"

