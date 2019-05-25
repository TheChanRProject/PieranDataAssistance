import os
import re
import shutil
class Git():

    def __init__(self, path, file):
        os.path.expanduser("~")
        self.path = path
        self.path_files = os.listdir(path)
        for i in self.path_files:
            if i.endswith(".txt"):
                self.full_path = os.path.join(path, file)
                self.file = open(self.full_path, "r")
            else:
                file_path = input("Please input a file path: ")
                self.full_path = os.path.join(file_path, file)
                self.file = open(, "r")
        os.chdir(self.path)  


    def clone(self):
        for i in self.file.readlines():
            x = i.replace("\n", "")
            os.system(f"git clone {x}")

myGit = Git(path="/Volumes/DSDRIVE/DS/Python/Udemy/Jose_Portilla/PieranDataAssistance/JAsen", file="file.txt")

myGit.clone()
