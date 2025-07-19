# This idea is partially stolen from the actual vm
from zipfile import ZipFile
import json
import io

from pygame import Vector2, image

from electrosb3.project.costume import Costume
from electrosb3.project.sprite import Sprite
import electrosb3.block_engine as BlockEngine

class Deserialize:
    def __init__(self, ProjectFile: ZipFile, Project):
        self.file = ProjectFile

        project_json = self.get_as_json("project.json")

        for target in project_json["targets"]: Project.sprites.append(self.deserialize_target(target))

        # lemme js sort by layer
        # just learned you could also just use a lambda for this
        Project.sprites.sort(key=lambda sprite: sprite.layer_order)

    def deserialize_costume(self, costume):
        image_file = self.get(costume["md5ext"])

        costume_object = Costume()
        costume_object.image = image.load(io.BytesIO(image_file))
        costume_object.rotation_center = Vector2(costume["rotationCenterX"],-costume["rotationCenterY"]) # HACK: For the displaying to work properly, we need to make rotationCenterY negative
        costume_object.name = costume["name"]

        return costume_object
    
    def deserialize_target(self, target):
        sprite = Sprite()

        if (not target["isStage"]): # The stage target always will not have any transformation info
            sprite.position = Vector2(target["x"],target["y"])
            sprite.size = target["size"]
            sprite.rotation = target["direction"]
            sprite.visible = target["visible"]
            sprite.layer_order = target["layerOrder"]

        print(target["blocks"])

        # Load costumes
        for costume in target["costumes"]: sprite.costumes.append(self.deserialize_costume(costume))

        sprite.setup() # Sorta temporary

        return sprite 

    # Get a file and return its bytes, If there is no file, a FileNotFound error is raised.
    def get(self, File: str):
        if File in self.file.namelist():
            return self.file.read(File)
        else:
            raise FileNotFoundError(File)
        
    def get_as_json(self, File: str): return json.loads(self.get(File))