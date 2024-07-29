#!/usr/bin/python3
"""
     export employee data tasks into CSV FORMAT
     Comma Seperated Values
"""

import csv
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    response = requests.get(url + "users/{}".format(emp_id))
    data = response.json()

    todo = requests.get(url + "todos?userId={}".format(emp_id))
    todo_data = todo.json()

    with open("{}.csv".format(emp_id), "w", newline='') as csvfile:
        col = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=col)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                "USER_ID": emp_id,
                "USERNAME": data['name'],
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
                })