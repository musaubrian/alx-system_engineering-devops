#!/usr/bin/python3
"""
send request to an API
"""

import csv
import requests
import sys


def send_request():
    """
    Sends a request for a json file
    """
    employee_id = sys.argv[1]
    user_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            )
    todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/"
            )

    employee_name = user_response.json().get('name')
    
    filename = employee_id + '.csv'
    with open(filename, 'a') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos_response.json():
            if task.get('userId') == int(employee_id):
                csv_writer.writerow([employee_id, employee_name, str(task.get('completed')),
                                 task.get('title')])

if __name__ == "__main__":
    send_request()
