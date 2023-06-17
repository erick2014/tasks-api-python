import logging
from flask import Blueprint, jsonify, request
from models import db, Task

tasks = Blueprint('todos', __name__)


@tasks.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    users_data = [task.serialize() for task in tasks]
    return jsonify(users_data)


@tasks.route('/tasks/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    pass


@tasks.route('/tasks', methods=['POST'])
def create_todo():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    state = 'new'
    new_user = Task(title, description, state)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='User created successfully')


@tasks.route('/tasks/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    pass


@tasks.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    pass
