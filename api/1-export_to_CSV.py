#!/usr/bin/python3
"""
Python script that, using the provided REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    response = requests.get(url)
    todos = response.json()
    employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json().get("name")
    user_id = argv[1]
    file_name = user_id + ".csv"

    with open(file_name, mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todos:
            writer.writerow(
                {
                    "USER_ID": user_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": task.get("completed"),
                    "TASK_TITLE": task.get("title")
                }
            )

    print("Data exported to file: {}".format(file_name))
