from models.task import TaskSchema, Task
from celeryapp.task import start_task


def getAllTasks():
    schema = TaskSchema()
    tasks = Task.query.all()
    return schema.dump(tasks, many=True)


def createTask():
    task = Task.addTask()

    start_task.apply_async(None, None, task.uuid)

    schema = TaskSchema()
    return schema.dump(task)

def getTaskByUuid(uuid):
    task = Task.query.filter_by(uuid=uuid).one()
    schema = TaskSchema()
    return schema.dump(task)
