import os

class Git():

    def __init__(self, file):
        self.path = os.getcwd()
        self.path_files = os.listdir(self.path)
        if file in self.path_files:
            self.full_path = os.path.join(self.path, file)
            self.file = open(self.full_path, "r")
        else:
            file_path = input("Please input a file path: ")
            self.full_path = os.path.join(file_path, file)
            self.file = open(self.full_path, "r")


    def clone(self):
        os.path.expanduser("~")
        os.chdir(self.path)
        for i in self.file.readlines():
            x = i.replace("\n", "")
            os.system(f"git clone {x}")

myGit = Git(file="file.txt")

myGit.clone()
