#!/usr/bin/python3
"""
Python script that, using the provided REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to CSV.
"""

import requests
import csv
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    response = requests.get(url)
    todos = response.json()
    employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json().get("name")

    total_tasks = len(todos)
    completed_tasks = sum(1 for task in todos if task.get("completed"))

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    with open('{}.csv'.format(argv[1]), mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos:
            writer.writerow({
                'USER_ID': argv[1],
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task.get("completed")),
                'TASK_TITLE': task.get("title")
            })
