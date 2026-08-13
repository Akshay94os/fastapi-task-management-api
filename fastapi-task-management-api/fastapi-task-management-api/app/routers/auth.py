from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.auth.jwt import create_access_token
from app.auth.security import hash_password,verify_password
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate,UserResponse
router=APIRouter(prefix="/auth",tags=["Authentication"])
@router.post("/register",response_model=UserResponse)
def register(data:UserCreate,db:Session=Depends(get_db)):
    if db.query(User).filter(User.email==data.email).first():raise HTTPException(400,"Email already registered")
    user=User(name=data.name,email=data.email,password=hash_password(data.password))
    db.add(user);db.commit();db.refresh(user);return user
@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(User).filter(User.email==form_data.username).first()
    if not user or not verify_password(form_data.password,user.password):raise HTTPException(401,"Invalid email or password")
    return {"access_token":create_access_token(user.id),"token_type":"bearer"}
