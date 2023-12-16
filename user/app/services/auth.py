from sqlalchemy import or_
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from ..schemas.auth import Token
from ..exceptions import Unauthorized
from ..config.auth import SECRET, EXP, ALGORITHM
from sqlalchemy.orm import Session
from ..models.user import UserModel
from ..models.user_pass import UserPass

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:

    def __init__(self, db: Session):
        self.__db = db

    @classmethod
    def hash(cls, password: str):
        return pwd_context.hash(password)

    @classmethod
    def verify(cls, plain: str, hashed: str):
        return pwd_context.verify(plain, hashed)

    @classmethod
    def encode(cls, data: dict, delta: timedelta | None = None) -> str:
        if delta:
            expire = datetime.utcnow() + delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=EXP)
        data.update({'exp':expire})
        encoded_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
        return encoded_token

    @classmethod
    def decode(cls, token: str) -> Token:
        try:
            decoded_token = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
            return Token(**decoded_token)
        except JWTError:
            raise Unauthorized

    def get(self, query:str, password: str) -> str | None:
        """Authenticate user and return a Bearer token
        """
        user = (
            self.__db.query(
                UserModel.id,
                UserModel.username,
                UserModel.email,
                UserPass.salt,
                UserPass.password,
            )
            .filter(or_(UserModel.username == query, UserModel.email == query))
            .outerjoin(UserPass, UserModel.id == UserPass.user_id)
            .first()
        )
        if not user:
            return None
        if self.verify(user.salt + password, user.password):
            data = Token(id=user.id, username=user.username, email=user.email).model_dump()
            return self.encode(data)

