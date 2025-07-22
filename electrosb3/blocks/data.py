import electrosb3.block_engine as BlockEngine

class BlocksData:
    def __init__(self):
        self.variables = {}

        self.block_map = {
            "setvariableto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.setvariableto
            },
        }

    def setvariableto(self, args, script):
        self.variables.update({args["VARIABLE"].id: args["VALUE"]})

BlockEngine.register_extension("data", BlocksData())