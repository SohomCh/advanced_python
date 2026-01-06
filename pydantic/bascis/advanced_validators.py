from pydantic import BaseModel,field_validator,computed_field

class Person(BaseModel):
    first_name:str
    last_name:str


    @field_validator('first_name','last_name')
    def name_must_be_capitalized(cls,v):
        if not v.istitle():
            raise ValueError('Names must be captialized')
        return v
    
    
    


class User(BaseModel):
    email:str

    @field_validator('email')
    def normalize(cls,v):
        return v.lower().strip()
    
class Product(BaseModel):
        price:str 

        @field_validator('price'mode=before)
        def parse_price(cls,v):
            if isinstance(v,str):
                return float(v.replace('$','').replace(',',''))

            return v
        
    
            


        
    


