#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    file_csv = sys.argv[1] + '.csv'
    id_emp = int(sys.argv[1])
    l, m = 0, 0
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    s = requests.get('https://jsonplaceholder.typicode.com/users')
    info_user = s.json()
    info_todos = r.json()

    with open(file_csv, mode='w') as csv_file:
        the_file = csv.writer(csv_file, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)

        for x in info_user:
            if id_emp == x.get("id"):
                user_name = (x.get("username"))
        for y in info_todos:
            if y.get("userId") == id_emp:
                the_file.writerow([str(id_emp), user_name, y.get("completed"),
                                   y.get("title")])
