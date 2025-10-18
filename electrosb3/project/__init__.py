from zipfile import ZipFile
from pathlib import Path

from electrosb3.project.deserialize import Deserialize
from electrosb3.project.sprite import Sprite
from electrosb3.block_engine.scriptstepper import ScriptStepper

import electrosb3.blocks as Blocks # Imported here to initalize blocks

class Project:
    def __init__(self, file):
        self.game_name = Path(file).stem

        self.sprites: list[Sprite] = []

        self.script_stepper = ScriptStepper()

        Deserialize(ZipFile(file, "r"), self)

        self.script_stepper.start_hats("event_whenflagclicked")

    def update(self, screen):
        for sprite in self.sprites:
            sprite.update(screen)

        self.script_stepper.step_scripts()