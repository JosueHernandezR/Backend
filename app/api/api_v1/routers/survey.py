from typing import Any, List

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from fastapi import APIRouter, Body, Depends, HTTPException, Security
from fastapi.encoders import jsonable_encoder
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app.crud.crud_survey import CRUDSurvey

router = APIRouter(prefix="/surveys", tags=["surveys"])

@router.post("/createSurvey", response_model=schemas.SurveyInDB)
def create_survey(*, db: Session = Depends(deps.get_db), survey_in: schemas.SurveyCreate, current_user: models.User = Security(deps.get_current_active_user),) -> Any:
    survey = crud.survey.create_user_survey(db, obj_in = survey_in)
    return survey

@router.get("", response_model=List[schemas.AnswerInDB])
def get_surveys(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100) -> Any:
    surveys = CRUDSurvey.get_all_surveys(db, skip=skip, limit=limit)
    return surveys

@router.put("/{survey_id}", response_model=schemas.SurveyInDB)
def update_survey(*, db: Session = Depends(deps.get_db), survey_id = UUID4, survey_in = schemas.SurveyUpdate, current_user: models.User = Security(deps.get_current_active_user)) -> Any:
    survey = crud.survey.get(db, id = survey_id)
    survey = crud.survey.update_survey(db, db_obj=survey, obj_in=survey_in)
    return survey