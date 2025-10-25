import electrosb3.block_engine.block_support as BlockSupport
import electrosb3.block_engine.extension_support as ExtensionSupport
import electrosb3.block_engine.enum as Enum

class Field:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Args:
    def __init__(self): pass

class Mutation:
    def __init__(self, raw):
        def has(value): return value in raw.keys()
        
        # im way too lazy
        if has("proccode"): self.proc_code = raw["proccode"]
        if has("argumentids"): self.args = raw["argumentids"]
        #if has("warp"): self.warp = raw["warp"]

        # ?
        if has("hasnext"): self.has_next = raw["hasnext"]

class InputReturnedNilException(Exception):
    """Exception raised for custom error in the application."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}, \nIt is possible that you defined an opcode with the wrong type, to prevent headaches, this custom exception handles this error."

class Block:   
    timer_end = 0

    def __init__(self, sprite):
        self.opcode = None
        self.set = None

        self.id = None

        self.info = {}

        self.next = None
        self.parent = None

        self.api = BlockSupport.API(sprite, self)

        self.sprite = sprite

        self.args = {}

    def get_opcode(self):
        return self.set+"_"+self.opcode

    def parse_fields(self, field): 
        if field[1] == None: return Field(field[0], None) # Return only the name
        else: return Field(field[0], field[1])

    def parse_input(self, input, script):
        blocks = self.api.stepper.blocks

        data = ExtensionSupport.get_block_set("data")

        wrapper_type = input[0]
        wrapper_value = input[1]

        if type(wrapper_value) == list: # Input is a simple number
            return self.parse_input(wrapper_value, script)
        elif wrapper_type >= 4 and wrapper_type <= 9: # All number literals
            return float(wrapper_value)
        elif wrapper_type == 10:
            return wrapper_value # string
        elif wrapper_type <= 3: # Input in block, or a substack
            if not (wrapper_value in blocks):
                debug_block = self.sprite.debug_blocks[wrapper_value]

                print(f"Couldn't get wrapped block! Missing opcode {debug_block["opcode"]}, fields: {debug_block["fields"]}, inputs: {debug_block["inputs"]}")

            block = blocks[wrapper_value]

            if block.info["type"] == Enum.BLOCK_INPUT: # For now, input blocks are ran recursively, 
                response = block.run_block(script)

                if response == None:
                    raise InputReturnedNilException(f"Opcode - {block.set + "_" + block.opcode}, ID - {block.id}, Sprite - {block.sprite.name}")

                return response 
            else: # Return so that it can be branched, i dont believe this is assuming anyth
                return block.id
        elif wrapper_type == 11: # Variable
            return input[1]
        elif wrapper_type == 12: # Variable
            return data.get_variable(input[2])
        else:
            pass

    def parse_only_fields(self):
        args = {}

        fields = self.args["fields"]

        for i in fields:
            args.update({i.lower():self.parse_fields(fields[i])})

        return args

    def parse_args(self, script):
        args = Args()

        inputs = self.args["inputs"]
        fields = self.args["fields"]

        for i in inputs:
            args.__dict__.update({i.lower():self.parse_input(inputs[i], script)})
        
        for i in fields:
            args.__dict__.update({i.lower():self.parse_fields(fields[i])})

        return args

    def run_block(self, script):
        self.api.set_script(script)
        self.api.loops += 1

        # TODO: Replace the script API with a better one
        return ExtensionSupport.run_block_func(self, self.parse_args(script), self.api)