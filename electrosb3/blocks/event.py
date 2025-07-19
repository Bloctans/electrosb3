import electrosb3.block_engine as Block

class Blocks_Event:
    def __init__(self):
        self.block_map = {
            "whenflagclicked": {
                "type": Block.BLOCK_HAT,
            }
        }

    def whenflagclicked():
        return True
    
Block.register_extension("event", Blocks_Event())