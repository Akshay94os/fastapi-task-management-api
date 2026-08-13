from datetime import datetime
from pydantic import BaseModel,ConfigDict,Field
class TaskCreate(BaseModel):
    title:str
    description:str|None=None
    priority:str="medium"
    due_date:datetime|None=None
class TaskUpdate(BaseModel):
    title:str|None=None
    description:str|None=None
    priority:str|None=None
    status:str|None=None
    due_date:datetime|None=None
class TaskResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:int
    user_id:int
    title:str
    description:str|None
    priority:str
    status:str
    due_date:datetime|None
    created_at:datetime
