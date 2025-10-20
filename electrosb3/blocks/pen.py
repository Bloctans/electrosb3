from electrosb3.block_engine import Enum, register_extension

class BlocksPen:
    def __init__(self):
        self.block_map = {
            "clear": {
                "type": Enum.BLOCK_STACK,
                "function": self.pass_block
            },
            "stamp": {
                "type": Enum.BLOCK_STACK,
                "function": self.pass_block
            }
        }

    def pass_block(self): pass

# This stays unregistered until we actually make progress on it
register_extension("pen", BlocksPen())