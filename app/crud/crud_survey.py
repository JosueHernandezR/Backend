from typing import Optional, Union, List, Dict, Any
from app import schemas

from app.crud.base import CRUDBase
from app.models.survey import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session

class CRUDSurvey(CRUDBase[Survey, SurveyCreate, SurveyUpdate]):
    def get_by_survey_id(self, db: Session, *, id:UUID4) -> Optional[Survey]:
        return db.query(self.model).filter(Survey.id == id).first()
    
    def get_all_surveys(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Survey]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create_user_survey(self, db: Session, *, survey: schemas.SurveyCreate, user_id: UUID4) -> Survey:
        db_obj = Survey(
            title = survey.title,
            owner_id = user_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_survey(self, db: Session, *, db_obj: Survey, obj_in: Union[SurveyUpdate, Dict[str, Any]],) -> Survey:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

survey = CRUDSurvey(Survey)