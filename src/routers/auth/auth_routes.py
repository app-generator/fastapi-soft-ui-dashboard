from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from helpers.database import get_db
from helpers.utils import verify
import schemas, models, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')

    access_token = oauth2.create_access_token(data = {"user_id" : user.id})

    return {
            "access_token" : access_token,
            "token_type" : "bearer"
        }