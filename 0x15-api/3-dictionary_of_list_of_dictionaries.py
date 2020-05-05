#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    s = requests.get('https://jsonplaceholder.typicode.com/users')
    info_user = s.json()
    info_todos = r.json()
    l = 0

    with open('todo_all_employees.json', mode='w') as json_file:
        info_json = {}
        for x in info_user:
            user_name = (x.get("username"))
        for y in info_todos:
            if l == 0:
                user = y.get("userId")
                info_json[user] = []
            info_json[user].append({"username": user_name,
                                    "task": y.get("title"),
                                    "completed": y.get("completed")})
            l += 1
        json.dump(info_json, json_file)
