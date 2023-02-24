#!/usr/bin/python3
"""
Python script that, using the provided REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data in JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    response = requests.get(url)
    todos = response.json()
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            argv[1])).json().get("name")

    total_tasks = len(todos)
    completed_tasks = sum(1 for task in todos if task.get("completed"))

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks))

    data = {}
    data[argv[1]] = []
    for task in todos:
        task_data = {}
        task_data["task"] = task.get("title")
        task_data["completed"] = task.get("completed")
        task_data["username"] = employee_name
        data[argv[1]].append(task_data)

    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump(data, f)
