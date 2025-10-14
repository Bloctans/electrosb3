from zipfile import ZipFile
from pathlib import Path

from electrosb3.project.deserialize import Deserialize
from electrosb3.project.sprite import Sprite

import electrosb3.blocks as Blocks # Imported here to initalize blocks

class Project:
    def __init__(self, file):
        self.game_name = Path(file).stem

        self.sprites: list[Sprite] = []

        Deserialize(ZipFile(file, "r"), self)

    def update(self, screen):
        for sprite in self.sprites:
            sprite.update(screen)