 # Esquemas Pydantic
from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class Response(BaseModel):
    detail: str
    result: Optional[T] = None


class Login(BaseModel):
    username: str
    password: str