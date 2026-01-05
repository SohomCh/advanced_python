from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    username:str

    @field_validator('username')  ##Decorator
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("Username length should be more than 4")
        return v
    



class SingupData(BaseModel):
    password:str
    confirm_password:str


    @model_validator(mode='after')
    def password_match(cls,v):
        if v.password != v.confirm_password:
            raise ValueError("password missmatch")
        return v
    
    