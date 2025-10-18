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
            },
            "playuntildone": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.playuntildone
            },
            "setvolumeto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.setvolumeto
            }
        }

    def sound_from_name(self, name, sounds):
        for sound in sounds:
            if sound.name == name: return sound

    def setvolumeto(self, args, api):
        pass # TODO

    def play(self, args, api):
        args.sound_menu.play()

    def playuntildone(self, args, api):
        if not ("channel_playing" in api.info.keys()):
            channel = args.sound_menu.play()
            print("channel", channel)
            api.info.update({
                "channel_playing": channel
            })
            api.do_yield()
        elif api.info["channel_playing"].get_busy():
            api.do_yield()
        else:
            api.info["channel_playing"] = None
    
    def sounds_menu(self, args, api):
        return self.sound_from_name(args.sound_menu.name, api.sprite.sounds)

    def stopallsounds(self, args, script):
        pass

BlockEngine.register_extension("sound", BlocksSound())