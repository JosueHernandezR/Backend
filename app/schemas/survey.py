from datetime import date, datetime
from typing import Optional, List

from pydantic import UUID4, BaseModel

from app.schemas.question import Question

class SurveyBase(BaseModel):
    title: str
    owner_id: UUID4

class SurveyCreate(SurveyBase):
    pass

class SurveyUpdate(SurveyBase):
    pass

class SurveyInDBBase(SurveyBase):
    id: UUID4
    create_at: datetime
    expire_at: datetime
    questions: List[Question]

    class Config:
        orm_mode: True

class Survey(SurveyInDBBase):
    pass

class SurveyInDB(SurveyInDBBase):
    pass