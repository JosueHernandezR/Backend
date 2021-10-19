from typing import Optional, Union, List, Dict, Any
from app import schemas

from app.crud.base import CRUDBase
from app.models.question_option import Question_option
from app.schemas.question_option import QuestionOptionCreate, QuestionOptionUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session

class CRUDQuestionOption(CRUDBase[Question_option, QuestionOptionCreate, QuestionOptionUpdate]):
    def get_by_question_option_id(self, db: Session, *, id:UUID4) -> Optional[Question_option]:
        return db.query(self.model).filter(Question_option.id == id).first()

    def create_question_option(self, db: Session, *, question_option: schemas.QuestionOptionCreate, question_id: UUID4) -> Question_option:
        db_obj = Question_option(
            name = question_option.name,
            text = question_option.text,
            weight = question_option.weight,
            question_id =question_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_question_option(self, db: Session, *, db_obj: Question_option, obj_in: Union[QuestionOptionUpdate, Dict[str, Any]]) -> Question_option:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

question_option = CRUDQuestionOption(Question_option)