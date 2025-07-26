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
        if not (id in self.variables): self.variables[id] = 0.0

    def get_variable(self, id):
        self.setup_variable(id)

        return self.variables[id]
    
    def set_variable(self, id, value): 
        self.setup_variable(id)
        self.variables[id] = value

    def setvariableto(self, args, script): self.set_variable(args.variable, args.value)

    def changevariableby(self, args, api):
        variable_id = args.variable.id

        variable = self.get_variable(variable_id)
        self.set_variable(variable_id, variable + float(args.value)) # Always assume this will be a float


BlockEngine.register_extension("data", BlocksData())