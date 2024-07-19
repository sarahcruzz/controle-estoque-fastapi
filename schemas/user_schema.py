from typing import Optional
from pydantic import BaseModel as SchemaBaseModel
#Como o SQL Alchemy tem o BaseModel dele, não poderemos confundir

class UserSchema(SchemaBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int    
    instrutor: str
    
    class config:
        from_atributes = True
