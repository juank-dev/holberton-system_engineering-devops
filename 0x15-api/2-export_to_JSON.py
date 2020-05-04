#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    file_csv = sys.argv[1] + '.json'
    id_emp = int(sys.argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    s = requests.get('https://jsonplaceholder.typicode.com/users')
    info_user = s.json()
    info_todos = r.json()

    with open(file_csv, mode='w') as csv_file:
        info_json = {}
        info_json[str(id_emp)] = []

        for x in info_user:
            if id_emp == x.get("id"):
                user_name = (x.get("username"))
        for y in info_todos:
            if y.get("userId") == id_emp:
                info_json[str(id_emp)].append({"task": y.get("title"),
                                               "completed": y.get("completed"),
                                               "username": user_name})
        json.dump(info_json, csv_file)
