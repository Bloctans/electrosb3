# Container for a block
class Block:
    def __init__(self):
        self.type = None
        self.opcode = None

        self.inputs = {}
        self.fields = {}

        self.parent = None
        self.next = None