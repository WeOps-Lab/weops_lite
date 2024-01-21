from typing import Optional

from pydantic import BaseModel


class UserTokenEntity(BaseModel):
    token: Optional[str]
    error_message: Optional[str]
    success: bool
