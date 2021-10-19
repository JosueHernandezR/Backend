from typing import Optional, Union, List, Dict, Any
from app import schemas

from app.crud.base import CRUDBase
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate, AnswerUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session


class CRUDAnswer(CRUDBase[Answer, AnswerCreate, AnswerUpdate]):
    def get_by_answer_id(self, db: Session, *, id:UUID4) -> Optional[Answer]:
        return db.query(self.model).filter(Answer.id == id).first()
    
    def get_all_answer_by_user(self, db: Session, surveyed_id=UUID4) -> List[Answer]:
        return db.query(self.model).filter(Answer.surveyed_id == surveyed_id).all
    
    def create_answer(self, db: Session, *, answer: AnswerCreate, user_id: UUID4, question_id: UUID4) -> Answer:
        db_obj = Answer(
            weight = answer.weight,
            open_answer = answer.open_answer,
            option_id = answer.option_id,
            question_id = question_id,
            surveyed_id = user_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

answer = CRUDAnswer(Answer)