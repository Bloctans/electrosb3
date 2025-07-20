import electrosb3.block_engine as BlockEngine

class BlocksMotion:
    def __init__(self):
        self.block_map = {
            "changexby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changexby
            }
        }

    def changexby(self):
        return True
    
BlockEngine.register_extension("motion", BlocksMotion())