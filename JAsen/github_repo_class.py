import os

class Git():

    def __init__(self, path, file):
        self.path = os.listdir(path)

        for i in self.path:
            if ".txt" in i:
                self.file = open(f"{path}/{file}", "r")
            else:
                file_path = input("Please input a file path: ")
                self.file = open(f"{file_path}/{file}", "r")

    def clone(self):
        for i in self.file.readlines():
            x = i.replace("\n", "")
            os.system(f"cd {self.path} && git clone {x}")
