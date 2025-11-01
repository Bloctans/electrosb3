from zipfile import ZipFile
from pathlib import Path

from electrosb3.project.deserialize import Deserialize
from electrosb3.project.sprite import Sprite
from electrosb3.block_engine.scriptstepper import ScriptStepper

from electrosb3.renderer.draw import Drawer

import electrosb3.blocks as Blocks # Imported here to initalize blocks

class Project:
    def __init__(self, file):
        self.game_name = Path(file).stem

        self.sprites: dict[Sprite] = {}

        self.script_stepper = ScriptStepper()
        self.drawer = Drawer()

        Deserialize(ZipFile(file, "r"), self)

        self.script_stepper.start_hats("event_whenflagclicked")

    def update(self, screen):
        self.drawer.update(screen)
        self.script_stepper.step_scripts()