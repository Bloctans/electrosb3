import electrosb3.block_engine as BlockEngine
from math import floor

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
            }
        }

    def switchcostumeto(self, args, script):
        sprite = script.sprite

        costume = args.costume or 0

        if type(costume) == float or type(costume) == int: 
            costume = script.sprite.costumes[floor(costume)]

        sprite.set_costume(costume)

    def costume(self, args, script):
        sprite = script.sprite

        return sprite.costume_from_name(args.costume)

# This stays unregistered until we actually make progress on it
BlockEngine.register_extension("looks", BlocksLooks())