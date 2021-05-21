#!/usr/bin/python3
"""
Authentication to holberton API
"""
import requests
import json
import os


class HolbertonAPI:
    """
    Class to request different information to holberton's API
    """
    
    def auth_holberton(self, email, password):
        """
        Method to authenticate a user to holberton school API 
        """
        api_key = "049e77911e17d893d5327f8e39717c82"
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
        if 'error' in result_login:
            print(result_login['error'])
            os.remove('checkerLogin.txt')
            data = self.validate_login()
            print(data)
            self.auth_holberton(data[0], data[1])
        return(result_login)
        

    def get_profile():
        """
        Method to get my profile from holberton platform
        """
        pass

    def get_project(self, **data_user):
        """
        Method to get project from holberton platform
        """
        print("*****into your project ID*********")
        id_project = int(input("What project do you want to see: "))
        token = data_user['auth_token']
        # url to requests a project info
        url = "https://intranet.hbtn.io/projects/{}.json?auth_token={}".format(id_project, token)

        #Call the request
        headers = {
                "Content-Type": "application/json"
                }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Something went wrong, check your password and email. Code Error:{}".format(response.status_code))
        else:
            project = response.json() # Parse json to a dict object
            tasks = project["tasks"] # Save all task in variable. This is a array of hashes with every task of the project
        return tasks

    def get_task():
        """
        Method to get a task from a project's holberton platform
        """
        pass

    def request_correction():
        """
        Method to ask for correction of a task
        """
        pass

    def get_correction_result():
        """
        Method to get correction result of a task
        """
        pass

    def validate_login(self):
        """
        Method to validate login
        """
        value = os.path.isfile('checkerLogin.txt') 

        if value:
            print("******************************")
            print("You already register\n")
            with open('checkerLogin.txt', 'r') as f:
                data = json.load(f)
            email = data['email']
            password = data['password']    
        else:
            print('\n\n*****************************')
            print('**********    ***************\n\n')
            email = input("Enter your code: ")
            password = input("Enter your password: ")
            obj = {'email': email, 'password': password}
            with open('checkerLogin.txt', 'w') as f:
                json.dump(obj, f)
        return([email, password])



