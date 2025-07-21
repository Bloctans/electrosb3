import electrosb3.block_engine.extension_support as ExtensionSupport

class Block:
    def __init__(self):
        self.block_set = None
        self.opcode = None

        self.next = None
        self.parent = None

        self.inputs = {}
        self.fields = {}

YIELD_NONE = 1 # Dont yield, continue to run blocks
YIELD = 2 # Yield and call the same block next frame
YIELD_TILL_NEXT_FRAME = 3 # Yield for a single frame

class Script: # TODO: prolly put this in a different file
    def __init__(self, block_engine):
        self.current_block = None
        self.start_block = None

        self.block_engine = block_engine
        
        self.running = False

        # This concept is stolen from the VM.
        self.yielding = YIELD_NONE

        self.sprite = None

    def set_yield(self, yield_type): self.yielding = yield_type
    
    def goto(block: str): pass

    def try_to_start(self): # Attempt to start the script
        hat_result = ExtensionSupport.run_block(self.start_block,{},None)
        if hat_result: self.running = True

    def update(self):
        """
            My idea for this is that we simply step through until a block decides the script should be paused
        """

        #print("Update script")

        if self.yielding == YIELD_TILL_NEXT_FRAME: self.set_yield(YIELD_NONE)

        while True: # forever until we yield.
            if (not self.running):
                self.try_to_start()
                break
            else:
                # Run block (TODO)
                if self.yielding == YIELD_NONE:
                    # Step block (TODO)
                    pass
                else: break # All other cases break.