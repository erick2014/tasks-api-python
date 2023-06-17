from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    description = Column(String(255))
    state = Column(String(50))

    def __init__(self, title, description, state):
        self.title = title
        self.description = description
        self.state = state

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'state': self.state
        }
