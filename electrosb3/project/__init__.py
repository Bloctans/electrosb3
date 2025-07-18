from zipfile import ZipFile
from pathlib import Path

from electrosb3.project.deserialize import Deserialize
from electrosb3.project.costume import Costume
from electrosb3.project.sprite import Sprite

class Project:
    def __init__(self, file):
        self.game_name = Path(file).stem

        self.sprites: list[Sprite] = []

        Deserialize(ZipFile(file, "r"), self)

    def update(self, screen):
        pass