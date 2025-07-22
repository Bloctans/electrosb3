import electrosb3.block_engine.extension_support as ExtensionSupport
import electrosb3.block_engine.enum as Enum

class Field:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Block:   
    def __init__(self):
        self.opcode = None
        self.id = None
        self.info = {}

        self.next = None
        self.parent = None

        self.sprite = None

        self.args = {}

    def parse_fields(self, field): 
        if field[1] == None: return field[0] # Return only the name
        else: return Field(field[0], field[1])

    def parse_input(self, input, script):
        blocks = self.sprite.blocks

        data = ExtensionSupport.get_block_set("data")

        wrapper_type = input[0]
        wrapper_value = input[1]

        if type(wrapper_value) == list: # Input is a simple number
            return self.parse_input(wrapper_value, script)
        elif wrapper_type > 3 and wrapper_type < 11: # All literals
            if wrapper_value.isdigit(): return float(wrapper_value) # Return float
            else: return wrapper_value # Return string
        elif wrapper_type < 4: # Input in block, or a substack
            if not (wrapper_value in blocks):
                debug_block = self.sprite.debug_blocks[wrapper_value]

                print(f"Couldn't get wrapped block! Missing opcode {debug_block["opcode"]}, fields: {debug_block["fields"]}, inputs: {debug_block["inputs"]}")

            block = blocks[wrapper_value]

            if block.info["type"] == Enum.BLOCK_INPUT: # Parse inputs normally
                return block.run_block(script)  
            else: # Return so that it can be branched, i dont believe this is assuming anyth
                return block.id
        elif wrapper_type == 12: # Variable
            return data.get_variable(input[2])
        else:
            pass

    def run_block(self, script):
        args = {}

        inputs = self.args["inputs"]
        fields = self.args["fields"]

        for i in inputs:
            args.update({i:self.parse_input(inputs[i], script)})
        
        for i in fields:
            args.update({i:self.parse_fields(fields[i])})

        #print(args)

        # TODO: Replace the script API with a better one
        return ExtensionSupport.run_block_func(self, args, script)