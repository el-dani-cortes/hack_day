#!/usr/bin/python3
"""
Create repo, directory and files
"""
import os


class CreateFiles:
    """
    Validate and create files needed in the holberton's project
    """

    def __init__(self, repo=None, directory=None, filename=None):
        """
        Save all the paths and names needed
        """
        self.repo = "./" + repo 
        self.directory = "/" + directory + "/" 
        self.filename = filename
    
    def create_repo(self)
        """
        Validate and create repository path
        """
        repo_exist = os.path.isdir(self.repo)
        if repo_exist is False:
            os.makedirs(self.repo)
        else:
            return None

    def create_directory(self):
        """
        Validate and create directory inside repository directory
        """
        path = self.repo + self.directory
        if path is False:
            os.makedirs(path)
        else:
            return None

    def create_file(self, tasks):
        """
        Validate and create files inside directory of the project
        """
        file_path = self.repo + self.directory + self.filename
        if file_path is False:
            with open(filepath, 'w') as file:
                file.write("""{}""".format(tasks["title"]))
        else:
            return None
