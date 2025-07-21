import electrosb3.block_engine as BlockEngine

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
            }
        }

    def changexby(self, args, script):
        sprite = script.sprite

        sprite.position.x += float(args["DX"])
    
    def changeyby(self, args, script):
        sprite = script.sprite

        sprite.position.y += float(args["DY"])
    
BlockEngine.register_extension("motion", BlocksMotion())