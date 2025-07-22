import electrosb3.block_engine as BlockEngine
from pygame import Vector2

class BlocksMotion:
    def __init__(self):
        self.block_map = {
            "changexby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changexby
            },
            "changeyby": { # did i do it right?
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changeyby
            },
            "gotoxy": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.gotoxy
            },
            "pointindirection": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.pointindirection
            },
            "xposition": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.xposition
            },
            "yposition": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.yposition
            },
            "setx": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.setx
            },
            "sety": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.sety
            }
        }

    def _changeby(x,y,sprite): sprite.position += Vector2(x,y)
    def _setrotation(self, rotation, sprite):
        pass

    def pointindirection(self, args, script):
        self._setrotation(args["DIRECTION"], script.sprite)

    def changexby(self, args, script): self._changeby(args["DX"],0,script.sprite)
    def changeyby(self, args, script): self._changeby(0,args["DY"],script.sprite)

    def gotoxy(self, args, script):
        script.sprite.position = Vector2(args["X"], args["Y"])

    def setx(self, args, script):
        print(args)

    def sety(self, args, script):
        print(args)

    def xposition(self, args, script): return script.sprite.position.x
    def yposition(self, args, script): return script.sprite.position.y
    
BlockEngine.register_extension("motion", BlocksMotion())