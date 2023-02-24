#!/usr/bin/python3
"""
Python script that, using the provided REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    response = requests.get(url)
    todos = response.json()
    employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json().get("name")

    total_tasks = len(todos)
    completed_tasks = sum(1 for task in todos if task.get("completed"))

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    for task in todos:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
