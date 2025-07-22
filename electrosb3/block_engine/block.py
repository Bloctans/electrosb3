import electrosb3.block_engine.extension_support as ExtensionSupport
import electrosb3.block_engine.enum as Enum

class Field:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Block:   
    def __init__(self):
        self.block_set = None
        self.opcode = None

        self.block_info = {}

        self.next = None
        self.parent = None

        self.sprite = None

        self.inputs = {}
        self.fields = {}

    # I do not know how we should properly handle these.
    def parse_fields(self, field): 
        if len(field) > 1:
            return Field(field[0], field[1])
        else:
            return field[0] # Return only the name

    def parse_input(self, input, script):
        blocks = self.sprite.blocks

        wrapper_type = input[0]
        wrapper_value = input[1]

        if type(wrapper_value) == list: # Input is a simple number
            return self.parse_input(wrapper_value, script)
        elif wrapper_type > 3 and wrapper_type < 11: # All literals
            if wrapper_value.isdigit():
                return float(wrapper_value)
            else:
                return wrapper_value
        elif wrapper_type == 2 or wrapper_type == 3: # Input in block, or a substack
            block = blocks[wrapper_value]

            if block.block_info["type"] == Enum.BLOCK_INPUT: # Parse inputs normally
                return block.run_block(script)  
            else: # Return so that it can be branched, i dont believe this is assuming anyth
                return block

    def run_block(self, script):
        inputs = {}

        for i in self.inputs:
            inputs.update({i:self.parse_input(self.inputs[i], script)})
        
        for i in self.fields:
            inputs.update({i:self.parse_fields(self.fields[i])})

        print(inputs)

        return ExtensionSupport.run_block_func(self, inputs, script)