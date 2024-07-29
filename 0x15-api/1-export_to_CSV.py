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

    user_data = requests.get(url + "users/{}".format(emp_id)).json()
    username = user_data.get("username")
    todo_data = requests.get(url + "todos", params={"userId": emp_id}).json()

    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            writer.writerow([
                 emp_id, username,
                 task.get("completed"),
                 task.get("title")
                 ])
