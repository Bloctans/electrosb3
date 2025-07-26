import electrosb3.block_engine as BlockEngine

class BlocksSound:
    def __init__(self):
        self.block_map = {
            "play": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.play
            },
            "sounds_menu": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.sounds_menu
            },
            "stopallsounds": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.stopallsounds
            }
        }

    def play(self, args, api):
        args.sound_menu.play()
    
    def sounds_menu(self, args, api):
        print(args.sound_menu)
        return api.sprite.sound_from_name(args.sound_menu.name)

    def stopallsounds(self, args, script):
        pass

BlockEngine.register_extension("sound", BlocksSound())