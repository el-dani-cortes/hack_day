#!/usr/bin/python3
"""
Create repo, directory and files
"""
import os


class CreateFile:
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
    
    def create_repo(self):
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
        dir_exist = os.path.isdir(path)
        if dir_exist is False:
            os.makedirs(path)
        else:
            return None

    def create_file(self, task):
        """
        Validate and create files inside directory of the project
        """
        total_files = self.filename.split(',')
        dir_shebang = {".js": "#!/usr/bin/node", ".py": "#!/usr/bin/python3", ".c": "/**\n*your comment here\n**/"}
        new_route = False
        for file in total_files:
            if file[-1:] == '/':
                path = self.repo + self.directory + file.strip()
                dir_exist = os.path.isdir(path)
                if dir_exist is False:
                    os.makedirs(path)
                    break
                else:
                    break
            elif "/" in file:
                new_route = True
                dirs = file.split("/")
                file = dirs[-1]
                dirs = dirs[:-1]
                route = ""
                for dir in dirs:
                    route += dir.strip() + "/"
                    path = self.repo + self.directory + dir.strip()
                    print(path)
                    dir_exist = os.path.isdir(path)
                    if dir_exist is False:
                        os.makedirs(path)
                
            if new_route:
                file_path = self.repo + self.directory + route + file.strip()
            else:
                file_path = self.repo + self.directory + file.strip()
        
            file_exist = os.path.isfile(file_path)
            if file_exist is False:
                if file_path[-3:] in dir_shebang or file_path[-2:] in dir_shebang:
                    if file_path[-2:] == ".c":
                        title = dir_shebang[file_path[-2:]]
                    else:
                        title = dir_shebang[file_path[-3:]]
                else:
                    title = "remember your general requirements"
                with open(file_path, 'w') as file:
                    file.write(title)
            else:
                return None
