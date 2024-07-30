#!/usr/bin/python3
"""
    Exports employees todo tasks into JSON FORMAT."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            data.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": data.get("username")
            } for task in requests.get(url + "todos", params={
                "userId": data.get("id")}).json()]
            for data in users}, jsonfile)
