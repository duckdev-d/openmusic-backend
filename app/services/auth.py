from typing import Annotated
from datetime import datetime
from datetime import timezone
from datetime import timedelta

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
import jwt
from jwt.exceptions import InvalidTokenError

from app.core.security import oauth2_scheme
from app.repositories.user import UserRepo
from app.core.security import verify_password
from app.core.config import settings
from app.schemas.token import TokenData


class AuthService:
    def __init__(self, db: UserRepo):
        self.repo = UserRepo(db)
        self.expires_delta = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.algorithm = settings.ALGORITHM
        self.secret_key = settings.SECRET_KEY

    def authenticate_user(self, username: str, password: str):
        user = self.repo.get_by_username(username)
        if not user:
            return False
        if not verify_password(password, user.password_hash):
            return False
        return user

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.expires_delta)
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username = payload.get('sub')
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except InvalidTokenError:
            raise credentials_exception
        user = self.repo.get_by_username(username=token_data.username)
        if user is None:
            raise credentials_exception
        return user
