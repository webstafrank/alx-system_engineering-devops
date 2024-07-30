#!/usr/bin/python3
"""
Fetching and exporting TODO list progress for a given employee ID
to a JSON file using a REST API.
"""

import json
import requests
import sys

def fetch_employee_data(employee_id):
    """Fetch employee data and TODO list from the API"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return None, None

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data

def export_to_json(employee_id, employee_name, todos):
    """Export TODO list data to a JSON file"""
    filename = f"{employee_id}.json"
    tasks = []
    for task in todos:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        }
        tasks.append(task_dict)

    data = {str(employee_id): tasks}
    with open(filename, mode='w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_data, todos_data = fetch_employee_data(employee_id)
    if not user_data or not todos_data:
        print("Employee not found.")
        sys.exit(1)

    employee_name = user_data.get('username')
    export_to_json(employee_id, employee_name, todos_data)
