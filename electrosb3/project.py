from zipfile import ZipFile
from pathlib import Path
from shutil import rmtree
import os.path
import json

class Project:
    def __init__(self, file):
        
        self.game_name = Path(file).stem

        with ZipFile(file, "r") as sb3:
            # print all contents of the sb3
            sb3.printdir()

            # extract the sb3
            if os.path.exists("./unpacked/"):
                rmtree("./unpacked/")
            sb3.extractall("./unpacked/")

        with open("./unpacked/project.json", "r", encoding="utf8") as project_file:
            self.data = json.load(project_file)
            print(self.data)
