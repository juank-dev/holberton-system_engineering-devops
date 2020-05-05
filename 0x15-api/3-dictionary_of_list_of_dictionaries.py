#!/usr/bin/python3
"""
Python script that, using this REST API, Records all tasks from all employees.
"""

if __name__ == "__main__":
    import json
    import requests

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    s = requests.get('https://jsonplaceholder.typicode.com/users')
    info_user = s.json()
    info_todos = r.json()

    with open('todo_all_employees.json', mode='w') as json_file:
        info_json = {}
        list_all = {}
        for x in info_user:
            user_name = x.get("username")
            my_id = x.get("id")
            l = 0
            for y in info_todos:
                if my_id == y.get("userId"):
                    if l == 0:
                        user = y.get("userId")
                        info_json[user] = []
                        l = 1
                    info_json[user].append({"username": user_name,
                                            "task": y.get("title"),
                                            "completed": y.get("completed")})
            list_all.update(info_json)
        json.dump(list_all, json_file)
