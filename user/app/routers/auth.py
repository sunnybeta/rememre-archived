from typing import Annotated
from fastapi import APIRouter, Body, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..services.auth import AuthService
from ..dependencies import get_db

router = APIRouter(prefix="/auth")


@router.post("/tokens")
def generate_tokens(user: Annotated[str, Body()], password: Annotated[str, Body()], db: Annotated[Session, Depends(get_db)]):
    token = AuthService(db).get(query=user, password=password)
    if not token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    return {'data':{'token':token}}

