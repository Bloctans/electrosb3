import electrosb3.block_engine.extension_support as ExtensionSupport

class Block:
    def __init__(self):
        self.block_set = None
        self.opcode = None

        self.next = None
        self.parent = None

        self.inputs = {}
        self.fields = {}

    def parse_input(self, input):
        pass