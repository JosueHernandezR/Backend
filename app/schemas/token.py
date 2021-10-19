from pydantic import UUID4, BaseModel

from app.schemas.user import UserBase


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: str
    user_info: UserBase


class TokenPayload(BaseModel):
    id: UUID4
