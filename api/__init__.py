from flask_restplus import Api, Resource

from .taskController import *

api = Api(
    version='1.0',
    title='API',
    description='api',
)

ns = api.namespace('api', description='task api namespace')

@ns.route('/tasks')
class TaskList(Resource):
    @api.doc('get all tasks')
    def get(self):
        return taskController.getAllTasks()

    @api.doc('start a task')
    def post(self):
        return taskController.createTask()


@ns.route('/tasks/<uuid>')
class Task(Resource):
    @api.doc('get a task')
    def get(self, uuid):
        return taskController.getTaskByUuid(uuid)
