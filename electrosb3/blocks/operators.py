import electrosb3.block_engine as BlockEngine

class BlocksOperator:
    def __init__(self):
        self.block_map = {
            "play": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.play
            },
            "sounds_menu": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.sounds_menu
            },
            "stopallsounds": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.stopallsounds
            }
        }

    def play(self, args, script):
        pass
    
    def sounds_menu(self, args, script):
        pass

    def stopallsounds(self, args, script):
        pass

# This stays unregistered until we actually make progress on it
#BlockEngine.register_extension("operator", BlocksOperator())