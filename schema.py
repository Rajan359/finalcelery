from pydantic import BaseModel, EmailStr, Field 
from models import User1,User2
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str="" 
    email: str= ""
    phonenumber: int= None
    city: str= ""
    state: str= ""


class UserUpdate(BaseModel):
    name: Optional[str] = ""
    email: Optional[str] = ""
    phonenumber: Optional[int] = None
    city: Optional[str] = ""
    state: Optional[str] = ""
    
# class UserUpdate(BaseModel):
#     name: Optional[str] = ""
#     email: Optional[str] = ""
#     phonenumber: Optional[int] = None
#     city: Optional[str] = ""
#     state: Optional[str] = ""
# class EmployeeBase(BaseModel):
#     name: str=""
#     email: str=""
#     phone_number: str=""
#     department: str=""
#     city: str=""
#     state: str=""

     






    