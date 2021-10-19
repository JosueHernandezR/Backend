from datetime import datetime
from typing import Optional, List

from pydantic import UUID4, BaseModel, EmailStr

from app.schemas.question_option import QuestionOption

class QuestionBase(BaseModel):
    question: str
    accept_open_answer: bool
    is_mandatory: bool
    survey_id: UUID4

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(QuestionBase):
    pass

class QuestionInDBBase(QuestionBase):
    id: UUID4
    question_options: List[QuestionOption]
    class Config:
        orm_mode = True

class Question(QuestionBase):
    pass

class QuestionInDB(QuestionInDBBase):
    pass