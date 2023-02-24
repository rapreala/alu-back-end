#!/usr/bin/python3
"""
Export data in CSV format
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    tasks_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))

    try:
        user_response.raise_for_status()
        tasks_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

    user = user_response.json()
    tasks = tasks_response.json()

    with open("{}.csv".format(employee_id), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            writer.writerow([employee_id, user['username'], task['completed'], task['title']])
