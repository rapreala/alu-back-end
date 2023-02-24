#!/usr/bin/python3
"""
Python script that, using the provided REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import json
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])
    response = requests.get(url)
    todos = response.json()
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            argv[1])).json().get("name")

    tasks = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        tasks.append(task_dict)

    data = {argv[1]: tasks}
    file_name = "{}.json".format(argv[1])
    with open(file_name, 'w') as f:
        json.dump(data, f)
