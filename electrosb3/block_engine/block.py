class Block:
    def __init__(self):
        self.type = None
        self.opcode = None

        self.next = None
        self.parent = None

        self.inputs = {}
        self.fields = {}

class Script:
    def __init__(self):
        self.current_block = None
        self.start_block = None

        self.blocks = {}
    
    def goto(block: str):
        pass

    def update(self):
        pass