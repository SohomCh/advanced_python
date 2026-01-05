from pydantic import BaseModel,Field
from typing import List,Optional,Dict


class Employee(BaseModel):
    id:int
    name:str =Field(

        ...,# it means required,
        min_length=3,
        max_length=50,
        description="Employee name",
        examples="Sohom Chatterjee"

        )
    department:Optional[str]='General'
    salary:float=Field(
        ...,
        ge=10000,
        le=1000000,
        description="Annual salary in $",

    )
    



