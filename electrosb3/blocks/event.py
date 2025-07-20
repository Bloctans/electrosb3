import electrosb3.block_engine as BlockEngine

class BlocksEvent:
    def __init__(self):
        self.block_map = {
            "whenflagclicked": {
                "type": BlockEngine.Enum.BLOCK_HAT,
            }
        }

    def whenflagclicked():
        return True
    
BlockEngine.register_extension("event", BlocksEvent())