import electrosb3.block_engine as BlockEngine

class BlocksEvent:
    def __init__(self):
        self.block_map = {
            "whenflagclicked": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.whenflagclicked
            }
        }

        self.started = False

    def whenflagclicked(self, args, script):
        startedold = self.started
        self.started = True

        return (not startedold)
    
BlockEngine.register_extension("event", BlocksEvent())