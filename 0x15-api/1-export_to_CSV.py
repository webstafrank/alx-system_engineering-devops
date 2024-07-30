#!/usr/bin/python3
"""
Fetching and displaying the TODO list progress for a given employee ID
using a REST API. It also exports the data to a CSV file.
"""

import csv
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

def display_todo_progress(employee_name, todos):
    """Display the TODO list progress for the employee"""
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

def export_to_csv(user_id, username, todos):
    """Export the TODO list to a CSV file"""
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get('completed'), task.get('title')])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

    employee_name = user_data.get('name')
    display_todo_progress(employee_name, todos_data)
    export_to_csv(employee_id, employee_name, todos_data)
