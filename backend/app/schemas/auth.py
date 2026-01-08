from pydantic import BaseModel, Field, validator
import re


class RegisterSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=128)

    @validator("username")
    def username_allowed_chars(cls, v):
        if not re.match(r"^[a-zA-Z0-9_-]+$", v):
            raise ValueError("Username can only contain letters, numbers, underscores and hyphens")
        return v

    @validator("password")
    def password_strength(cls, v):
        # at least one lowercase, one uppercase and one digit
        if not re.search(r"[a-z]", v) or not re.search(r"[A-Z]", v) or not re.search(r"\d", v):
            raise ValueError("Password must include uppercase, lowercase and digits")
        return v


class LoginSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=128)


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
