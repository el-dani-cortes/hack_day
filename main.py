#!/usr/bin/python3

from holbertonAPI import HolbertonAPI
from create_files import CreateFile
import json
import os
import sys

while (True):
        user = HolbertonAPI()
        data_user = user.validate_login()
        data_user = user.auth_holberton(data_user[0], data_user[1], data_user[2])
        if 'error' not in data_user:
            break
        print(data_user['error'])
        os.remove('checkerLogin.txt')

if len(sys.argv) == 1:
    print(data_user)
    while (True):
        token = data_user['auth_token']
        id_project = int(input("What project do you want to see: "))
        tasks = user.get_project(token, id_project)
        if tasks != "Not Found":
            break
        else:
            print("That project doesn't exist, enter a new one")

    for task in tasks:
        new_file = CreateFile(task['github_repo'], task['github_dir'], task['github_file'])
        new_file.create_repo()
        new_file.create_directory()
        new_file.create_file(task)
elif len(sys.argv) == 2:
    id_project = sys.argv[1]
    token = data_user['auth_token']
    tasks = user.get_project(token, id_project)
    for task in tasks:
        task_info = user.get_task(task['id'], token)
        if task_info['checker_available'] is True:
            ask_correction = user.request_correction(task['id'], token)
            results = user.get_correction_result(ask_correction, token)
            print(results)
        else:
            print("The task: {} must request a manual review".format(task['title']))
else:
    pass

