from pydantic import BaseModel
from uuid import UUID
from typing import List

class UserListResponse(BaseModel):
    users: List[UserOut]

    class Config:
        orm_mode = True