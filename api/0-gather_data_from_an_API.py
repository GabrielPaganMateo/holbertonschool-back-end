#!/usr/bin/python3
"""
Pythin script that uses this 
rest api for given employee ID to return
info about his/her todo list progress
"""
from sys import argv
from requests import get
import json
"""this module is fucking documented"""

employee_ID = argv[1]
employee_info = get(f'https://jsonplaceholder.typicode.com/todos/{employee_ID}')
all_todos = get(f'https://jsonplaceholder.typicode.com/todos')

employee_dict = json.loads(employee_info.text)
employee_list = json.loads(all_todos.text)


employee_name = employee_dict['userId']
completed_task = 0
task_count = 0
task_list = []
for employee in employee_list:
    if employee['userId'] == employee_dict['userId']:
        task_count += 1
        if employee['completed'] == True:
            completed_task += 1
            task_list.append(employee['title'])
        


print(f'Employee {employee_name} is done with tasks({completed_task}/{task_count}):')

for task in task_list:
    print(f'     {task}')