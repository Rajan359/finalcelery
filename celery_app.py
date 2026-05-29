from celery import Celery

celery = Celery(
    "sync_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["tasks"]
)
# celery.conf.beat_schedule = {

#     "sync-every-10-seconds": {

#         "task": "tasks.sync_tables",

#         "schedule": 5.0
#     }
# }