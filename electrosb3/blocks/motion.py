import electrosb3.block_engine as BlockEngine
from pygame import Vector2
from math import sin, cos, radians

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
            },
            "movesteps": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.move_steps
            },
            "turnright": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.turnright
            },
            "direction": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.direction
            }
        }

    # TODO: Rewrite motion extension

    def _changeby(self,x,y,util): 
        util.sprite.position += Vector2(x,y)
        util.request_redraw()

    def _setrotation(self, rotation, sprite): 
        sprite.rotation = rotation
        
    def _changerotation(self, rotation, sprite): 
        sprite.rotation += rotation

    def pointindirection(self, args, util): 
        self._setrotation(args.direction, util.sprite)

    def direction(self, args, util): return util.sprite.rotation

    def changexby(self, args, util): 
        self._changeby(args.dx,0,util)

    def changeyby(self, args, util): 
        self._changeby(0,args.dy,util)

    def gotoxy(self, args, util): 
        util.request_redraw()
        util.sprite.position = Vector2(args.x, args.y)

    def setx(self, args, util): 
        util.request_redraw()
        util.sprite.position.x = float(args.x)

    def sety(self, args, util):
        util.request_redraw()
        util.sprite.position.y = float(args.y)

    def xposition(self, args, util): return util.sprite.position.x
    def yposition(self, args, util): return util.sprite.position.y

    def turnright(self, args, util): 
        util.request_redraw()
        self._changerotation(float(args.degrees), util.sprite)

    def move_steps(self, args, util):
        sprite = util.sprite
        steps = float(args.steps)

        rotation = radians(sprite.rotation)

        self._changeby(
            sin(rotation)*steps,
            cos(rotation)*steps,
            util
        )
    
BlockEngine.register_extension("motion", BlocksMotion())