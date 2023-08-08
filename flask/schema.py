import pydantic
from typing import Optional, Type


class CreateUser(pydantic.BaseModel):
    username: str
    password: str

    @pydantic.validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password is too short")
        return value


class PatchUser(pydantic.BaseModel):
    username: Optional[str]
    password: Optional[str]

    @pydantic.validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password is too short")
        return value


class CreateAd(pydantic.BaseModel):
    user_id: int
    description: str
    heading: str


class PatchAd(pydantic.BaseModel):
    description: Optional[str]
    heading: Optional[str]


VALIDATION_CLASS = Type[CreateUser] | Type[PatchUser] | Type[CreateAd] | Type[PatchAd]