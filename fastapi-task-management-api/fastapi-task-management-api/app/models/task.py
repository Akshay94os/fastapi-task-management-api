from datetime import datetime
from sqlalchemy import Column,DateTime,ForeignKey,Integer,String,Text
from app.database import Base
class Task(Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    title=Column(String(200),nullable=False)
    description=Column(Text)
    priority=Column(String(20),default="medium",nullable=False)
    status=Column(String(20),default="pending",nullable=False)
    due_date=Column(DateTime,nullable=True)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
