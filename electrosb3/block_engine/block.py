import electrosb3.block_engine.extension_support as ExtensionSupport

class Block:   
    def __init__(self):
        self.block_set = None
        self.opcode = None

        self.next = None
        self.parent = None

        self.sprite = None

        self.inputs = {}
        self.fields = {}

    def parse_input(self, input, script):
        blocks = self.sprite.blocks

        wrapper_type = input[0]
        wrapper_value = input[1]

        if wrapper_type == 1: # Input is a simple number
            return self.parse_input(wrapper_value, script)
        elif wrapper_type == 2 or wrapper_type == 3: # Block in block
            return blocks[wrapper_value].run_block(script)
        elif wrapper_type > 3 and wrapper_type < 11: # All literals
            return wrapper_value
        else: # Not implemented.
            return None     

    def run_block(self, script):
        inputs = {}

        for i in self.inputs:
            inputs.update({i:self.parse_input(self.inputs[i], script)})

        return ExtensionSupport.run_block_func(self, inputs, script)