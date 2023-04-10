#!/usr/bin/python3
""" Console Module """
"""
Pythin script that uses this  rest api for given
employee ID to return info about his/her todo list progress
"""
if __name__ == '__main__':
    import csv
    import json
    from requests import get
    from sys import argv
    """this module is fucking documented"""

    employee_ID = argv[1]
    all_todos = get(f'https://jsonplaceholder.typicode.com/todos')
    users = get(f'https://jsonplaceholder.typicode.com/users')

    employee_list = json.loads(all_todos.text)
    users = json.loads(users.text)
    for user in users:
        if user.get('id') == int(employee_ID):
            employee_name = user.get('username')

    task_count = 0
    task_list = []
    task_success = []
    for employee in employee_list:
        if employee.get('userId') == int(employee_ID):
            task_count += 1
            task_list.append(employee['title'])
            task_success.append(employee['completed'])

    csv_list = []
    employee_id = str(employee_ID)
    for i in range(len(task_list)):
        line = eval(f"['{employee_id}', '{employee_name}', '{task_success[i]}', '{task_list[i]}']")
        csv_list.append(line)
    
    with open(f'{employee_ID}.csv', mode='w') as f:
        f = csv.writer(f, quoting=1)
    
        for list in csv_list:
            f.writerow(list)


"""
    firstline = (
        f'Employee {employee_name} is done'
        f' with tasks({completed_task}/{task_count}):'
    )
    print(firstline)

    for task in task_list:
        print(f'\t {task}')"""
