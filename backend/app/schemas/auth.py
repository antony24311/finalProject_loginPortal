from pydantic import BaseModel


class RegisterSchema(BaseModel):
    username: str
    password: str


class LoginSchema(BaseModel):
    username: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
