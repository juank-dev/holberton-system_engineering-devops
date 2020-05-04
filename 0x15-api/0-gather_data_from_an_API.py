#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    id_emp = int(sys.argv[1])
    l, m = 0, 0
    title = []

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    s = requests.get('https://jsonplaceholder.typicode.com/users')
    print("Employee ", end="")
    info_user = s.json()
    info_todos = r.json()
    for x in info_user:
        if id_emp == x.get("id"):
            print(x.get("name"), end=" is done with tasks")
    for y in info_todos:
        if y.get("userId") == id_emp:
            l += 1
            if y.get("completed") is True:
                m += 1
                title.append(y.get("title"))
    print("({}/{}):".format(m, l))
    for z in title:
        print("\t {}".format(z))
