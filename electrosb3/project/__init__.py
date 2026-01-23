from zipfile import ZipFile
from pathlib import Path

from electrosb3.project.deserialize import Deserialize
from electrosb3.project.sprite import Sprite
from electrosb3.block_engine.scriptstepper import ScriptStepper
from electrosb3.block_engine import Enum

import electrosb3.util as Util

from electrosb3.renderer.draw import Drawer

import electrosb3.blocks as Blocks # Imported here to initalize blocks

class Project:
    def __init__(self, file, name = "Unknown"):
        if type(file) == str:
            self.game_name = Path(file).stem
        else:
            self.game_name = name

        self.sprites: dict[Sprite] = {}

        self.script_stepper = ScriptStepper()
        self.drawer = Drawer()

        Deserialize(ZipFile(file, "r"), self)

        self.script_stepper.start_hats("event_whenflagclicked")

    def push_event(self, event):
        if event == Enum.MOUSE_DOWN:
            def sprite_clicked(hat, sprite):
                if Util.is_touching("_mouse_", sprite):
                    #for variable in sprite.variables:
                    #    print(sprite.variables[variable].__dict__)
                        
                    self.script_stepper.create_script(hat, sprite)

            self.script_stepper.each_hat("event_whenthisspriteclicked", {}, sprite_clicked, True)
        else:
            print("Invalid event!")

    def update(self, screen):
        self.drawer.update(screen)
        self.script_stepper.step_scripts()