import electrosb3.block_engine as BlockEngine

class BlocksProcedures:
    def __init__(self):
        self.block_map = {
            "definition": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.definition
            },
        }

    def definition(self, args, api):
        pass

BlockEngine.register_extension("procedures", BlocksProcedures())