import electrosb3.block_engine.enum as Enum
from electrosb3.block_engine.block import Block

class Script:
    def __init__(self):
        self.current_block = None
        self.start_block = None

        self.step_next = None # Value set by a block that determines what to step to next

        self.stack = []

        self.running = False
        self.yielding = Enum.YIELD_NONE # This concept is stolen from the VM.

        self.sprite = None

    def is_yielding(self): return (self.yielding == Enum.YIELD)
    def set_yield(self, yield_type): 
        self.yielding = yield_type

    #  This concept is once again... DRUMROLL.............. Stolen from the VM!!!!!!
    def branch_to(self, block: str, loop: bool): 
        self.step_next = block
        self.stack.append([self.current_block, loop])

    def goto(self, block: str): 
        if type(block) == Block:
            self.current_block = block
        else:
            self.current_block = self.get_block(block)

    def step_block(self):
        #print(self.current_block.opcode)
        if self.current_block.next == None: # Stop the script if there is no next
            if len(self.stack) > 0:  # Check if stack has any data
                stack_last = self.stack.pop()

                if stack_last[1] == True:
                    #print("loop")
                    self.goto(stack_last[0])
                else:
                    #print("go to next")
                    self.current_block = stack_last[0]
                    self.step_block()

                return
            #print("stopping")
            self.running = False
        else: # Otherwise, go to next
            self.goto(self.current_block.next)

    def run_block(self, block): 
        return block.run_block(self)
    
    def get_block(self, id): 
        if not (id in self.sprite.blocks):
            debug_block = self.sprite.debug_blocks[id]

            print(f"Couldn't get block! Missing opcode {debug_block["opcode"]}, fields: {debug_block["fields"]}, inputs: {debug_block["inputs"]}")

        return self.sprite.blocks[id]

    def update(self):
       # print(self.yielding)

        if self.yielding == Enum.YIELD_TILL_NEXT_FRAME: 
            self.set_yield(Enum.YIELD_NONE)
            self.step_block()

        while True: # forever until we yield.
            if (not self.running):
                self.current_block = self.start_block
                hat_result = self.run_block(self.current_block)
                if hat_result: 
                    self.running = True
                    self.step_block()

                break
            else:
                #print(self.current_block.opcode)
                self.run_block(self.current_block)

                if self.step_next: # Custom step
                    self.goto(self.step_next)
                    self.step_next = None
                elif self.yielding == Enum.YIELD_NONE: self.step_block()
                else: break # All other cases break.