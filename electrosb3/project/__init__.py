from zipfile import ZipFile
from pathlib import Path

from electrosb3.project.deserializer import Deserialize
from electrosb3.project.skin import Skin
from electrosb3.project.sprite import Sprite

class Project:
    def __init__(self, file):
        self.game_name = Path(file).stem

        self.sprites = []

        Deserialize(ZipFile(file, "r"), self)

    def update(self, screen):
        pass