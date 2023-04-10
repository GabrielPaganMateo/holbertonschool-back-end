#!/usr/bin/python3
""" Console Module """
"""
Pythin script that uses this  rest api for given
employee ID to return info about his/her todo list progress
"""
if __name__ == '__main__':
    import json
    from requests import get
    from sys import argv
    """this module is fucking documented"""

    all_todos = get(f'https://jsonplaceholder.typicode.com/todos')
    users = get(f'https://jsonplaceholder.typicode.com/users')

    employee_list = json.loads(all_todos.text)
    users = json.loads(users.text)

    task_count = 0
    task_list = []
    task_success = []
    for employee in employee_list:
        task_list.append(employee['title'])
        task_success.append(employee['completed'])

    json_list = []
    THE_dict = {}
    user_count = 0
    for user in users:
        user_count += 1
        employee_name = user.get('username')
        for i in range(len(task_list)):
            true_or_false = bool(task_success[i])
            task = f'{task_list[i]}'
            name = employee_name
            every_dict = ({'username': name,
                           'task': task,
                           'completed': true_or_false})
            json_list.append(every_dict)
        THE_dict[str(user_count)] = json_list

    print(THE_dict)
    with open('todo_all_employees.json', 'w') as f:
        json.dump(THE_dict, f)