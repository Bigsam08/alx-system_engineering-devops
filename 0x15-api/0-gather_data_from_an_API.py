#!/usr/bin/python3
"""
    get the TODO LISTS of an employee using REST API
     accepts an integer parameter (employeee id) and display result
     in JSON FORMAT
"""

import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    response = requests.get(url + "users/{}".format(emp_id))
    data = response.json()
    employee_name = data['name']

    todo = requests.get(url + "todos?userId={}".format(emp_id))
    todo_data = todo.json()

    completed_task = []
    for task in todo_data:
        if task["completed"]:
            completed_task.append(task)
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_task), total_tasks))
    for task in completed_task:
        print(f"\t {task['title']}")
