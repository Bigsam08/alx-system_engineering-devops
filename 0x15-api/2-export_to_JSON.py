#!/usr/bin/python3
"""
    Export employee data tasks into  JSON FORMAT
"""

import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(emp_id)).json()
    username = user_data.get("username")
    todo_data = requests.get(url + "todos", params={"userId": emp_id}).json()

    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump({emp_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                } for task in todo_data]}, jsonfile)
