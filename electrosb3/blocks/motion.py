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
            }
        }

    # TODO: Rewrite motion extension

    def _changeby(self,x,y,api): 
        api.sprite.position += Vector2(x,y)
        api.request_redraw()

    def _setrotation(self, rotation, sprite): 
        sprite.rotation = rotation
        
    def _changerotation(self, rotation, sprite): 
        sprite.rotation += rotation

    def pointindirection(self, args, script): 
        self._setrotation(args.direction, script.sprite)

    def changexby(self, args, script): 
        self._changeby(args.dx,0,script)

    def changeyby(self, args, script): 
        self._changeby(0,args.dy,script)

    def gotoxy(self, args, script): 
        script.request_redraw()
        script.sprite.position = Vector2(args.x, args.y)

    def setx(self, args, script): 
        script.request_redraw()
        script.sprite.position.x = float(args.x) # TODO: Properly convert digits

    def sety(self, args, script):
        print(args)

    def xposition(self, args, script): return script.sprite.position.x
    def yposition(self, args, script): return script.sprite.position.y

    def turnright(self, args, script): 
        script.request_redraw()
        self._changerotation(float(args.degrees), script.sprite)

    def move_steps(self, args, api):
        sprite = api.sprite
        steps = args.steps

        rotation = radians(sprite.rotation)

        self._changeby(
            sin(rotation)*steps,
            cos(rotation)*steps,
            api
        )
    
BlockEngine.register_extension("motion", BlocksMotion())