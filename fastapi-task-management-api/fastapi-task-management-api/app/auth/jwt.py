from datetime import datetime,timedelta,timezone
from jose import jwt
from app.database import settings
def create_access_token(user_id:int)->str:
    payload={"sub":str(user_id),"exp":datetime.now(timezone.utc)+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)}
    return jwt.encode(payload,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
