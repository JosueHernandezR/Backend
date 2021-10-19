from datetime import datetime
from typing import Optional, List

from pydantic import UUID4, BaseModel, EmailStr

class AnswerBase(BaseModel):
    weight: int
    open_answer: Optional[str]

    option_id: Optional[UUID4]
    question_id: UUID4
    surveyed_id: UUID4

class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
    pass

class AnswerInDBBase(AnswerBase):
    id: UUID4
    answered_at: datetime

    class Config:
        orm_mode = True

class Answer(AnswerInDBBase):
    pass

class AnswerInDB(AnswerInDBBase):
    pass