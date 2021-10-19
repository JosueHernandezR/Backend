from typing import Optional, List

from pydantic import UUID4, BaseModel

class QuestionOptionBase(BaseModel):
    name: str
    text: str
    weight: int
    question_id: UUID4

class QuestionOptionCreate(QuestionOptionBase):
    pass

class QuestionOptionUpdate(QuestionOptionBase):
    pass

class QuestionOptionInDBBase(QuestionOptionBase):
    id: UUID4

    class Config: 
        orm_mode = True

class QuestionOption(QuestionOptionInDBBase):
    pass

class QuestionOptionInDB(QuestionOptionInDBBase):
    pass