#!/usr/bin/python3

from holbertonAPI import HolbertonAPI
from create_files import CreateFile
import json
import os

user = HolbertonAPI()
data_user = user.validate_login()
data_user = user.auth_holberton(data_user[0], data_user[1])
print(data_user)
tasks = user.get_project(**data_user)


for task in tasks:
    new_file = CreateFile(task['github_repo'], task['github_dir'], task['github_file'])
    new_file.create_repo()
    new_file.create_directory()
    new_file.create_file(task)

