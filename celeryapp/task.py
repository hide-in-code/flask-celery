from . import celery_app
from models import db
from models.task import Task

celery_app = celery_app

@celery_app.task(bind=True)
def start_task(self):
    task_uuid = self.request.id
    task_db = db.session.query(Task).filter_by(uuid=task_uuid)
    task_db.update({"status": "completed"})
    db.session.commit()
    print('task: %s is done.' % task_uuid)


