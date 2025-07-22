import electrosb3.block_engine as BlockEngine

class BlocksData:
    def __init__(self):
        self.variables = {}

        self.block_map = {
            "setvariableto": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.setvariableto
            },
            "changevariableby": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.changevariableby
            }
        }

    def setup_variable(self, id): 
        if not (id in self.variables): self.variables[id] = 0

    def get_variable(self, id):
        self.setup_variable(id)

        return self.variables[id]
    
    def set_variable(self, id, value): 
        self.setup_variable(id)
        self.variables[id] = value

    def setvariableto(self, args, script): self.set_variable(args["VARIABLE"], args["VALUE"])

    def changevariableby(self, args, script):
        variable_id = args["VARIABLE"].id

        self.set_variable(variable_id, self.get_variable(variable_id) + args["VALUE"])

BlockEngine.register_extension("data", BlocksData())