class Block:
    def __init__(self):
        self.block_set = None
        self.type = None
        self.opcode = None

        #self.data = {}

        self.next = None
        self.parent = None

        self.inputs = {}
        self.fields = {}
    
    # Run the block and return a value
    def run():
        pass

YIELD_NONE = 1 # Dont yield, continue to run blocks
YIELD = 2 # Yield and call the same block next frame
YIELD_TILL_NEXT_FRAME = 3 # Yield for a single frame

class Script:
    def __init__(self):
        self.current_block = None
        self.start_block = None
        
        # This concept is stolen from the VM.
        self.yielding = YIELD_NONE

        self.blocks = {}

    def set_yield(self, yield_type): self.yielding = yield_type
    
    def goto(block: str):
        pass

    def step_block():
        pass

    def update(self):
        """
            My idea for this is that we simply step through until a block decides the script should be paused
        """

        match self.yielding:
            case 1: # Step block as normal
                self.step_block()
            case 2: # Pass, call the same block again.
                pass
            case 3: # It's the next frame. Set to none then step block.
                self.set_yield(YIELD_NONE)
                self.step_block()
            case _: # Pass, invalid!
                pass