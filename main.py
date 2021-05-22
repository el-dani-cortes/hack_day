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
            print("********** \033[92m{}\033[00m ***********".format("Successful Login"))
            print("+-------------------------------------+")
            break
        print("*********** {} ************".format(data_user['error']))
        os.remove('checkerLogin.txt')

if len(sys.argv) == 1:
    while (True):
        token = data_user['auth_token']
        id_project = int(input("Enter the project id that you want to create: "))
        tasks = user.get_project(token, id_project)
        if tasks != "Not Found" and tasks != None:
            break
        else:
            print("That project doesn't exist, enter a new one")

    for task in tasks:
        new_file = CreateFile(task['github_repo'], task['github_dir'], task['github_file'])
        new_file.create_repo()
        new_file.create_directory()
        new_file.create_file(task)
    print("+-------------------------------------+")
    print("***** \033[92mAll files have been created\033[00m *****")
    print("+-------------------------------------+")
    print("******** \033[93mYou can begin to code\033[00m ********")
    print("+-------------------------------------+")
elif len(sys.argv) == 2:
    id_project = sys.argv[1]
    token = data_user['auth_token']
    tasks = user.get_project(token, id_project)
    if tasks == "Not Found" or tasks is None:
        print("***** \033[31mProject id wrong, try again\033[00m *****")
        print("+-------------------------------------+")
    else:
        for task in tasks:
            task_info = user.get_task(task['id'], token)
            print("\033[5m\033[96m{}: {}...\033[00m".format('Checking task', task_info['title']))
            print("***************************************")
            if task_info['checker_available'] is True:
                ask_correction = user.request_correction(task['id'], token)
                results = user.get_correction_result(ask_correction, token)
                for result in results:
                    print("{} => {}   {} -->".format(result['title'], result['passed'], result['check_label']), end=" ")
                    if result['passed'] is True:
                            print("\033[92mCheck passed!\033[00m")
                    else:
                            print("\033[31mCheck failed!\033[00m")
                print("***************************************")
            else:
                print("\033[95mThe task: must request a manual review\033[00m")
else:
    id_project = sys.argv[1]
    id_task = int(sys.argv[2]) + 1
    token = data_user['auth_token']
    tasks = user.get_project(token, id_project)
    if tasks == "Not Found" or tasks is None:
        print("***** \033[31mProject id wrong, try again\033[00m *****")
        print("+-------------------------------------+")
    else:
        for task in tasks:
            if task['position'] == id_task:
                break
        task_info = user.get_task(task['id'], token)
        print("\033[5m\033[96mChecking task: {}...\033[00m".format(task_info['title']))
        print("***************************************")
        if task_info['checker_available'] is True:
            ask_correction = user.request_correction(task['id'], token)
            results = user.get_correction_result(ask_correction, token)
            for result in results:
                print("{} => {}   {} -->".format(result['title'], result['passed'], result['check_label']), end=" ")
                if result['passed'] is True:
                        print("\033[92mCheck passed!\033[00m")
                if result['passed'] is False:
                        print("\033[31mCheck failed!\033[00m")
            print("***************************************")
        else:
            print("\033[95mThe task: must request a manual review\033[00m")
