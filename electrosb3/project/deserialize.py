# This idea is partially stolen from the actual vm
from zipfile import ZipFile, ZipInfo
import json
import operator

from pygame import Vector2

from electrosb3.project.sprite import Sprite
from electrosb3.project.costume import Costume

class Deserialize:
    def __init__(self, ProjectFile: ZipFile, Project):
        self.file = ProjectFile

        project_json = self.get_as_json("project.json")

        for target in project_json["targets"]: Project.sprites.append(self.deserialize_target(target))

        # lemme js sort by layer
        Project.sprites.sort(key=operator.attrgetter("layer_order"))

    def deserialize_target(self, target):
        sprite = Sprite()

        if (not target["isStage"]): # The stage target always will not have any transformation info
            sprite.position = Vector2(target["x"],target["y"])
            sprite.size = target["size"]
            sprite.rotation = target["direction"]
            sprite.visible = target["visible"]
            sprite.visible = target["layerOrder"]

        for costume in target["costumes"]: # Load costumes
            sprite.costumes.append(Costume(self.get(costume["md5ext"]), (costume["rotationCenterX"], costume["rotationCenterY"]), costume["name"]))

        return sprite 

    # Get a file and return its bytes, If there is no file, a FileNotFound error is raised.
    def get(self, File: str):
        if File in self.file.namelist():
            return self.file.read(File)
        else:
            raise FileNotFoundError(File)
        
    def get_as_json(self, File: str): return json.loads(self.get(File))