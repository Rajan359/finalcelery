
from database import SessionLocal
from schema import UserCreate,UserUpdate
from models import User4,User1
from fastapi import FastAPI, Depends, HTTPException,WebSocketException,status


def sync_tables_student():
    db = SessionLocal()

    try:
        print("SYNC RUNNING 🚀")

        table1_rows = db.query(User1).all()

        for row1 in table1_rows:

            row2 = db.query(User4).filter(
                User4.id == row1.id
            ).first()
            if not row2:

                new_user = User4(
                    id=row1.id,
                    name=row1.name if row1.name else "",
                    email=row1.email if row1.email else "",
                    phonenumber=row1.phonenumber if row1.phonenumber else "",
                    city=row1.city if row1.city else "",
                    state=row1.state if row1.state else ""
                )
                db.add(new_user)
                # save_history(db, row1, "INSERT")
                continue
            updated = False

            for col in ["name", "email", "phonenumber", "city", "state"]:

                val1 = getattr(row1, col)
                val2 = getattr(row2, col)
                val1 = val1 if val1 else ""
                val2 = val2 if val2 else ""
                if val1 != val2:
                    setattr(row2, col, val1)
                    updated = True
            # if updated:
            #     save_history(db, row1, "UPDATE")

        db.commit()

    except Exception as e:
        db.rollback()
        print("SYNC ERROR:", e)

    finally:
        db.close()