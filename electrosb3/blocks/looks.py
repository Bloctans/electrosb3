import electrosb3.block_engine as BlockEngine

class BlocksLooks:
    def __init__(self):
        self.block_map = {
            "switchcostumeto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.switchcostumeto
            },
            "costume": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.costume
            },
            "nextcostume": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.nextcostume
            },
            "changesizeby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changesizeby
            },
            "setsizeto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changesizeby
            },
            "hide": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide
            },
            "show": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.show
            },
            "size": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.size
            }
        }

    def costume_from_name(self, name, costumes):
        for costume in costumes:
            if costume.name == name: return costume

    def hide(self, args, api): api.sprite.visible = False
    def show(self, args, api): api.sprite.visible = True

    def switchcostumeto(self, args, api):
        sprite = api.sprite

        costume = args.costume or 0

        sprite.set_costume(costume)

    def size(self, args, api):
        return 100

    def changesizeby(self, args, api):
        pass

    def nextcostume(self, args, api):
        sprite = api.sprite

        sprite.set_costume(sprite.current_costume.id+1)

    def costume(self, args, script):
        sprite = script.sprite

        return self.costume_from_name(args.costume, sprite.costumes)

# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("looks", BlocksLooks())