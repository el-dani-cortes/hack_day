#!/usr/bin/python3
"""
Authentication to holberton API
"""
import requests
import json
import os
from getpass import getpass

class HolbertonAPI:
    """
    Class to request different information to holberton's API
    """
    
    def auth_holberton(self, email, password, api_key):
        """
        Method to authenticate a user to holberton school API 
        """
        url = "https://intranet.hbtn.io/users/auth_token.json"
        data = {
            "api_key": api_key,
            "email": email + "@holbertonschool.com",
            "password": password,
            "scope": "checker"
        }
        header = {
            'Content-Type': 'application/json'
        }

        result_login = requests.post(url, data=json.dumps(data), headers=header).json()
        return(result_login)
        

    def get_profile():
        """
        Method to get my profile from holberton platform
        """
        pass

    def get_project(self, token, id_project):
        """
        Method to get project from holberton platform
        """
        # url to requests a project info
        url = "https://intranet.hbtn.io/projects/{}.json?auth_token={}".format(id_project, token)

        #Call the request
        headers = {
                "Content-Type": "application/json"
                }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Something went wrong, check your password and email. Code Error:{}".format(response.status_code))
            tasks = response.json()["error"]
        else:
            try:
                project = response.json() # Parse json to a dict object
                tasks = project["tasks"] # Save all task in variable. This is a array of hashes with every task of the project
            except:
                return None
        return tasks

    def get_task(self, id_task, token):
        """
        Method to get a task from a project's holberton platform
        """
        url = "https://intranet.hbtn.io/tasks/{}.json?auth_token={}".format(id_task, token)
        header = {
            'Content-Type': 'application/json'
        }
        task_info = requests.get(url, headers=header).json()
        return(task_info)
        

    def request_correction(self, id_task, token):
        """
        Method to ask for correction of a task
        """
        url = "https://intranet.hbtn.io/tasks/{}/start_correction.json?auth_token={}".format(id_task, token)
        header = {
            'Content-Type': 'application/json'
        }
        ask_correction = requests.post(url, headers=header).json()
        if ask_correction == None:
            print("The correction can’t be queued now")
        return(ask_correction)
        

    def get_correction_result(self, ask_correction_id, token):
        """
        Method to get correction result of a task
        """
        url = "https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}".format(str(ask_correction_id['id']), token)
        header = {
            'Content-Type': 'application/json'
        }
        while (True):
            result = requests.get(url, headers=header).json()
            if result['status'] == 'Done':
                checks = result['result_display']['checks']    
                return(checks)
            

    def validate_login(self):
        """
        Method to validate login
        """
        value = os.path.isfile('checkerLogin.txt') 

        if value:
            print("**************************************")
            print("****** You are already register ******")
            print("**************************************")
            with open('checkerLogin.txt', 'r') as f:
                data = json.load(f)
            email = data['email']
            password = data['password']
            api_key = data['api_key']    
        else:
            print("**************************************")
            email = input("Enter your holberton's code: ")
            password = getpass('Enter your password: ')
            api_key = input("Enter your API key: ")
            obj = {'email': email, 'password': password, "api_key": api_key}
            with open('checkerLogin.txt', 'w') as f:
                json.dump(obj, f)
        return([email, password, api_key])
