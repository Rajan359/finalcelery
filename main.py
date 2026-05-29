from genericpath import exists
from fastapi import FastAPI
from sqlalchemy import text
from database import SessionLocal
from fastapi import FastAPI, Depends, HTTPException,WebSocketException,status
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import threading
import time
from datetime import datetime, timezone as UTC
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
import pyodbc
from fastapi import FastAPI
from tasks import sync_tables
import models,schema
from schema import UserCreate,UserUpdate
from models import User1,User2,User4
models.Base.metadata.create_all(bind=engine)
from sync_service import sync_tables_student
from tasks import sync_tables
app = FastAPI()
scheduler = BackgroundScheduler(
    job_defaults={"max_instances": 1, "coalesce": False}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/tableemployee")
def get_data(db: Session = Depends(get_db)):
    try:
            result=db.query(User1).all()
            return {"data":result,"status":status.HTTP_200_OK}
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@app.get("/attendance")
def get_data(db: Session = Depends(get_db)):
    try:
            result=db.query(User2).all()
            return {"data":result,"status":status.HTTP_200_OK}
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/student")
def get_data(db: Session = Depends(get_db)):
    try:
            result=db.query(User4).all()
            return {"data":result,"status":status.HTTP_200_OK}
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@app.post("/insert")
def insert_data(user:UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User1(name=user.name, email=user.email,phonenumber=user.phonenumber,city=user.city,state=user.state)
        if db_user.name is exists and db_user.email is exists:
            return{
                "message":"User Already Exist",
                # "data":db_user,
                "status":status.HTTP_400_BAD_REQUEST
            }
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": "Data Inserted Successfully","data":db_user,"status":status.HTTP_201_CREATED}
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=str(e))



@app.put("/update/{user_name}/")
def update_data(user_name: str, user: UserUpdate, db: Session = Depends(get_db)):

    try:
        db_user = db.query(User1).filter(User1.name == user_name).first()

        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Step 1: get only provided fields
        update_data = user.dict(exclude_unset=True)

        # Step 2: update DB object
        for key, value in update_data.items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)

        # Step 3: build FULL merged response (old + new)
        full_data = {
            "name": db_user.name,
            "email": db_user.email,
            "phonenumber": db_user.phonenumber,
            "city": db_user.city,
            "state": db_user.state
        }

        return {
            "message": "Data Updated Successfully",
            "data": full_data,
            "status": 200
        }

    except HTTPException as e:
        raise e
    


@app.post("/sync")
def trigger_sync():

    task = sync_tables.delay()
    print("Sync Task Triggered:", task.id)

    return {
        "task_id": task.id
    }

       
@app.on_event("startup")
def start_scheduler():
    try:

        scheduler.add_job(
            sync_tables_student,
            "interval",
            seconds=5,
            id="sync_job",
            replace_existing=True
        )
 

        if not scheduler.running:
            scheduler.start()

        print("Scheduler Started 🚀")

    except Exception as e:
        print("Scheduler Start Error:", e)

@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()