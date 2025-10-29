import electrosb3.block_engine as BlockEngine

class BlocksData:
    def __init__(self):
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

            # TODO
            "lengthoflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.hide_variable
            },
            "itemoflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.hide_variable
            },
            "replaceitemoflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.hide_variable
            },
            "deletealloflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.hide_variable
            },
            "addtolist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.hide_variable
            },
            "itemnumoflist": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.hide_variable
            },
            "listcontainsitem": {
                "type": BlockEngine.Enum.BLOCK_INPUT,
                "function": self.hide_variable
            }
        }
    
    def hide_variable(self, args, util):
        return 0

    def setvariableto(self, args, util): 
        util.set_variable(args.variable.id, args.value)

    def changevariableby(self, args, util):
        variable_id = args.variable.id

        variable = float(util.get_variable(variable_id).value)
        util.set_variable(variable_id, variable + float(args.value)) # Always assume this will be a float


BlockEngine.register_extension("data", BlocksData())