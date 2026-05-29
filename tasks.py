# from celery_app import celery
# from sync_service import sync_data

# @celery.task
# def run_sync_task():
#     sync_data()
#     return "Sync Completed"


from celery_app import celery
from database import SessionLocal
from models import User1, User2,User4

@celery.task
def sync_tables():

    db = SessionLocal()

    try:
        print("Celery  RUNNING 🚀")

        table1_rows = db.query(User1).all()

        for row1 in table1_rows:

            row2 = db.query(User2).filter(
                User2.id == row1.id
            ).first()

            # INSERT
            if not row2:

                new_user = User2(
                    id=row1.id,
                    name=row1.name or "",
                    email=row1.email or "",
                    phonenumber=row1.phonenumber or "",
                    city=row1.city or "",
                    state=row1.state or ""
                )

                db.add(new_user)

                continue

            # UPDATE
            for col in ["name", "email", "phonenumber", "city", "state"]:

                val1 = getattr(row1, col) or ""
                val2 = getattr(row2, col) or ""

                if val1 != val2:
                    setattr(row2, col, val1)

        db.commit()

        print("Celery  SYNC SUCCESS ✅")

    except Exception as e:
        db.rollback()
        print("Celery  SYNC ERROR ❌", e)

    finally:
        db.close()



