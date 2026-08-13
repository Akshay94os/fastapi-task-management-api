from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate,TaskResponse,TaskUpdate
router=APIRouter(prefix="/tasks",tags=["Tasks"])
@router.post("/",response_model=TaskResponse)
def create_task(data:TaskCreate,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    if data.priority not in {"low","medium","high"}:raise HTTPException(400,"Priority must be low, medium or high")
    task=Task(user_id=user.id,**data.model_dump())
    db.add(task);db.commit();db.refresh(task);return task
@router.get("/",response_model=list[TaskResponse])
def list_tasks(status:str|None=Query(None),priority:str|None=Query(None),db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    q=db.query(Task).filter(Task.user_id==user.id)
    if status:q=q.filter(Task.status==status)
    if priority:q=q.filter(Task.priority==priority)
    return q.order_by(Task.due_date.asc().nullslast(),Task.id.desc()).all()
@router.get("/{task_id}",response_model=TaskResponse)
def get_task(task_id:int,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==task_id,Task.user_id==user.id).first()
    if not task:raise HTTPException(404,"Task not found")
    return task
@router.put("/{task_id}",response_model=TaskResponse)
def update_task(task_id:int,data:TaskUpdate,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==task_id,Task.user_id==user.id).first()
    if not task:raise HTTPException(404,"Task not found")
    values=data.model_dump(exclude_unset=True)
    if "priority" in values and values["priority"] not in {"low","medium","high"}:raise HTTPException(400,"Invalid priority")
    if "status" in values and values["status"] not in {"pending","in_progress","completed","cancelled"}:raise HTTPException(400,"Invalid status")
    for k,v in values.items():setattr(task,k,v)
    db.commit();db.refresh(task);return task
@router.patch("/{task_id}/complete",response_model=TaskResponse)
def complete_task(task_id:int,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==task_id,Task.user_id==user.id).first()
    if not task:raise HTTPException(404,"Task not found")
    task.status="completed";db.commit();db.refresh(task);return task
@router.delete("/{task_id}")
def delete_task(task_id:int,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==task_id,Task.user_id==user.id).first()
    if not task:raise HTTPException(404,"Task not found")
    db.delete(task);db.commit();return {"message":"Task deleted successfully"}
@router.get("/summary/stats")
def task_summary(db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    tasks=db.query(Task).filter(Task.user_id==user.id).all()
    return {"total":len(tasks),"pending":sum(t.status=="pending" for t in tasks),"in_progress":sum(t.status=="in_progress" for t in tasks),"completed":sum(t.status=="completed" for t in tasks),"cancelled":sum(t.status=="cancelled" for t in tasks)}
