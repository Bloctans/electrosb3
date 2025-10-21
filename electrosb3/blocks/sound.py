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
            "playuntildone": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.playuntildone
            },
            "stopallsounds": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.stopallsounds
            },
            "setvolumeto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": lambda args, util: print("Unimplemented")
            }
        }

        self.sounds_playing = {}

    def sound_from_name(self, name, sounds):
        for sound in sounds:
            if sound.name == name: return sound

    def play_base(self, sound, util):
        channel = sound.play()
        self.sounds_playing.update({
            util.block.id: channel
        })

    def play(self, args, util): self.play_base(args.sound_menu, util)

    def playuntildone(self, args, util):
        sound_entry = None

        if not (util.block.id in self.sounds_playing):
            self.play_base(args.sound_menu, util)
            util.do_yield()
            print("Start sound entry")
        else:
            sound_entry = self.sounds_playing[util.block.id]

            if sound_entry.get_busy():
                print("Yielding play")
                util.do_yield()
            else:
                self.sounds_playing.pop(util.block.id)
    
    def stopallsounds(self, args, util):
        for sound in self.sounds_playing:
            sound.stop()
            self.sounds_playing.pop(sound)

    def sounds_menu(self, args, util):
        return self.sound_from_name(args.sound_menu.name, util.sprite.sounds)

BlockEngine.register_extension("sound", BlocksSound())