import electrosb3.block_engine.enum as Enum
from electrosb3.block_engine.block import Block

class Script:
    def __init__(self, block_engine):
        self.current_block = None
        self.start_block = None

        self.step_next = None # Value set by a block that determines what to step to next

        self.stack = []

        self.block_engine = block_engine
        
        self.running = False

        self.yielding = Enum.YIELD_NONE # This concept is stolen from the VM.

        self.sprite = None


    def is_yielding(self): return (self.yielding == Enum.YIELD)
    def set_yield(self, yield_type): 
        self.yielding = yield_type

    def branch_to(self, block: str): 
        self.step_next = block
        self.stack.append(self.current_block)

    def goto(self, block: str): 
        if type(block) == Block:
            self.current_block = block
        else:
            self.current_block = self.get_block(block)

    def step_block(self):
        print(self.current_block.opcode)
        if self.current_block.next == None: # Stop the script if there is no next
            if len(self.stack) > 0:  # Check if stack has any data
                self.goto(self.stack.pop())
                return
                
            print("stopping")
            self.running = False
        else: # Otherwise, go to next
            self.goto(self.current_block.next)

    def run_block(self, block): return block.run_block(self)
    def get_block(self, id): 
        if not (id in self.sprite.blocks):
            debug_block = self.sprite.debug_blocks[id]

            print(f"Couldn't get block! Missing opcode {debug_block["opcode"]}, fields: {debug_block["fields"]}, inputs: {debug_block["inputs"]}")

        return self.sprite.blocks[id]

    def update(self):
        #print("Update script")

        if self.yielding == Enum.YIELD_TILL_NEXT_FRAME: self.set_yield(Enum.YIELD_NONE)

        while True: # forever until we yield.
            if (not self.running):
                self.current_block = self.start_block
                hat_result = self.run_block(self.current_block)
                if hat_result: 
                    self.running = True
                    self.step_block()

                break
            else:
                self.run_block(self.current_block)

                if self.step_next: # Custom step
                    self.goto(self.step_next)
                    self.step_next = None
                elif self.yielding == Enum.YIELD_NONE: self.step_block()
                else: break # All other cases break.