from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from sqlalchemy.orm import Session
from app.database import get_db,settings
from app.models.user import User
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    error=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid authentication credentials")
    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        uid=payload.get("sub")
        if uid is None: raise error
    except (JWTError,ValueError): raise error
    user=db.query(User).filter(User.id==int(uid)).first()
    if not user: raise error
    return user
