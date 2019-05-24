import os
import re

class Git():

    def __init__(self, path, file):
        self.path = path
        self.path_files = os.listdir(path)
        for i in self.path_files:
            if re.match(".txt", i):
                self.file = open(f"{path}/{file}", "r")
            else:
                file_path = input("Please input a file path: ")
                self.file = open(f"{file_path}/{file}", "r")

    def clone(self):
        for i in self.file.readlines():
            x = i.replace("\n", "")
            os.system(f"cd ~/{self.path} && git clone {x}")

myGit = Git(path="/Volumes/DSDRIVE/DS/Python/Udemy/Jose_Portilla/PieranDataAssistance/JAsen", file="file.txt")

myGit.clone()
