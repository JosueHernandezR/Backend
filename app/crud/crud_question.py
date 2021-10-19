from typing import Dict, Any, Optional, Union
from app import schemas

from app.crud.base import CRUDBase
from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session

class CRUDQuestion(CRUDBase[Question,QuestionCreate, QuestionUpdate]):
    def get_by_question_id(self, db: Session, *, id:UUID4) -> Optional[Question]:
        return db.query(self.model).filter(Question.id == id).first()
    
    # def get_all_question_for_survey(self, db: Session, *, survey_id=UUID4) -> Optional[Question]:
    #     return db.query(self.model).filter(Question.survey_id == survey_id).all()

    def create_question(self, db: Session, *, question: QuestionCreate, survey_id:UUID4) -> Question:
        db_obj = Question(
            question = question.question,
            accept_open_answer = question.accept_open_answer,
            is_mandatory = question.is_mandatory,
            survey_id = survey_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_survey(self, db: Session, *, db_obj: Question, obj_in: Union[QuestionUpdate, Dict[str, Any]],) -> Question:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
question = CRUDQuestion(Question)