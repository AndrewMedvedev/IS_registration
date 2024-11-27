from pydantic import BaseModel, Field, field_validator
from email_validator import validate_email
import phonenumbers
from fastapi import HTTPException , status


class UserModel(BaseModel):
    phone_number: str = Field(default=..., description="Номер телефона в международном формате, начинающийся с '+'")
    email: str = Field(default=...,min_length=5, max_length=100, description="Электронная почта ")
    hash_password : str = Field(default=...,description="Пароль")
    first_name: str = Field(default=...)
    last_name: str = Field(default=...)
    first_name_fa: str = Field(default=...)
    birthday: str = Field(default=...)
    city_birthday: str = Field(default=...)

    
    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        parsed_number = phonenumbers.parse(values)
        if phonenumbers.is_valid_number(parsed_number):
            return values
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр"
            )
            

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if validate_email(value):
            return value
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email не соответствует формату"
            )


class GetUser(BaseModel):
    email:  str = Field(default=...,min_length=5, max_length=100, description="Электронная почта ")
    hash_password: str = Field(default=...,description="Пароль")
    
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if validate_email(value):
            return value
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email не соответствует формату"
            )
            
            
class RefreshUser(BaseModel):
    email:  str = Field(default=...,min_length=5, max_length=100, description="Электронная почта ")
    hash_password: str = Field(default=...,description="Пароль")
    new_hashpass : str = Field(default=...,description="Пароль")
            

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if validate_email(value):
            return value
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email не соответствует формату"
            )
    
    
    @field_validator("new_hashpass")
    @classmethod
    def validate_new_hashpass(cls, value: str) -> str:
        mesyac = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
        if value.lower() not in mesyac:
            return value
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="пароль не соответствует формату"
            )