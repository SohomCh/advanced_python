## recursive models in pydantic


from typing import List,Optional
from pydantic import BaseModel

class Commnet(BaseModel):
    id:int
    content:str
    replies:Optional[List['Commnet']]=None

Commnet.model_rebuild()

comment=Commnet(
    id=1,
    content="First Commnet",
    replies=[
        Commnet(id=2,content='reply'),
        Commnet(id=3,content="reply2",replies=[
            Commnet(id=4,content='reply3')
        ])
    ]

)