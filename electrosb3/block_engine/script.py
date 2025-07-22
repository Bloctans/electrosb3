import electrosb3.block_engine.enum as Enum

class Script:
    def __init__(self, block_engine):
        self.current_block = None
        self.start_block = None

        self.step_next = None # Value set by a block that determines what to step to next

        self.block_engine = block_engine
        
        self.running = False

        self.yielding = Enum.YIELD_NONE # This concept is stolen from the VM.

        self.sprite = None

    def is_yielding(self): return (self.yielding == Enum.YIELD)
    def set_yield(self, yield_type): self.yielding = yield_type

    def step_next_to(self, block: str): self.step_next = block
    def goto(self, block: str): self.current_block = self.get_block(block)

    def step_block(self):
        print(self.current_block.opcode)
        if self.current_block.next == None: # Stop the script if there is no next
            self.running = False
        else: # Otherwise, go to next
            self.goto(self.current_block.next)

    def try_to_start(self): # Attempt to start the script
        self.current_block = self.start_block
        hat_result = self.run_block(self.current_block)
        if hat_result: 
            self.running = True
            self.step_block()

    def run_block(self, block): return block.run_block(self)
    def get_block(self, id): return self.sprite.blocks[id]

    def update(self):
        #print("Update script")

        if self.yielding == Enum.YIELD_TILL_NEXT_FRAME: self.set_yield(Enum.YIELD_NONE)

        while True: # forever until we yield.
            if (not self.running):
                self.try_to_start()
                break
            else:
                self.run_block(self.current_block)

                if self.step_next: # Custom step
                    self.goto(self.step_next)
                    self.step_next = None
                elif self.yielding == Enum.YIELD_NONE: self.step_block()
                else: break # All other cases break.