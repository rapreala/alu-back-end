#!/usr/bin/python3
"""
Using a given employee ID, exports data in CSV format of all tasks owned by the employee.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    # Check for correct usage
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print(f"Usage: {sys.argv[0]} employee_id")
        sys.exit(1)

    # Get the employee ID and retrieve the user data
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to get user data: {user_response.status_code}")
        sys.exit(1)
    user_data = user_response.json()

    # Get the TODO list for the employee
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Failed to get TODO list: {todo_response.status_code}")
        sys.exit(1)
    todo_data = todo_response.json()

    # Save the TODO list in a CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            csv_writer.writerow([employee_id, user_data["username"], task["completed"], task["title"]])

    print(f"Data exported to {csv_filename} successfully.")
