from app import app 
from all_tasks.tasks import tasks_list


@app.route('/')
def index():
    return f'this is the index page'

@app.route('/tasks')
def get_all_tasks():
    tasks = tasks_list
    return tasks

@app.route('/tasks/<int:task_id>')
def get_task_by_id(task_id):
    tasks = tasks_list
    for task in tasks:
        if task['id'] == task_id:
            return task
    return {'error': f'A task with the ID of {task_id} does not exist'}, 404 

