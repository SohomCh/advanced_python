from typing import List,Optional

from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address


    