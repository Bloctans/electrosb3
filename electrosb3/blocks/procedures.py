import electrosb3.block_engine as BlockEngine

class BlocksProcedures:
    def __init__(self):
        self.block_map = {
            "definition": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.definition
            },
            "prototype": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.prototype
            },
            "call": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.prototype
            },
        }

    def definition(self, args, util):
        pass

    def prototype(self, args, util):
        pass

class BlocksArg:
    def __init__(self):
        self.block_map = {
            "reporter_string_number": {
                "type": BlockEngine.Enum.BLOCK_HAT,
                "function": self.definition
            },
            "argument_reporter_boolean": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.prototype
            },
        }

    def definition(self, args, util):
        pass

    def prototype(self, args, util):
        pass

BlockEngine.register_extension("procedures", BlocksProcedures())
BlockEngine.register_extension("argument", BlocksArg())