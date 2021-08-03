from . import db
from uuid import uuid4
from marshmallow import Schema, fields



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<UUID %r>' % self.uuid

    def addTask(self):
        task = Task()
        task.uuid = str(uuid4())
        task.status = 'running'

        db.session.add(task)
        db.session.commit()

        return task


class TaskSchema(Schema):
    uuid = fields.Str()
    status = fields.Str()
