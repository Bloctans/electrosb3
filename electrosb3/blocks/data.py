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
            },
            "hidevariable": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide_variable
            },
            "showvariable": {
                "type": BlockEngine.Enum.BLOCK_STACK,
                "function": self.hide_variable
            },
        }

    def setup_variable(self, id): 
        if not (id in self.variables): self.variables[id] = 0.0

    def get_variable(self, id):
        self.setup_variable(id)

        return self.variables[id]
    
    def hide_variable(self, args, util):
        pass
    
    def set_variable(self, id, value): 
        self.setup_variable(id)
        #print(f"{id}: {value}")
        self.variables[id] = value

    def setvariableto(self, args, script): 
        self.set_variable(args.variable.id, args.value)

    def changevariableby(self, args, util):
        variable_id = args.variable.id

        variable = float(self.get_variable(variable_id))
        self.set_variable(variable_id, variable + float(args.value)) # Always assume this will be a float


BlockEngine.register_extension("data", BlocksData())