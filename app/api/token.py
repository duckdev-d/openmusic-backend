from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.schemas.token import Token
from app.services.auth import AuthService
from app.core.db import get_session


router = APIRouter(prefix='/token', tags=['jwt'])


@router.post('/')
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_session)],
):
    auth_service = AuthService(db)
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token = auth_service.create_access_token(data={'sub': user.username})
    return Token(access_token=access_token, token_type='bearer')
