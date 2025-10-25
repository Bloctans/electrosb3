import electrosb3.block_engine.enum as Enum
from electrosb3.block_engine.block import Block

class StackEntry:
    def __init__(self, block, is_loop, stack_parent):
        self.parent = stack_parent
        self.block = block
        self.is_loop = is_loop

"""
    Yielding will stop the thread dead in its tracks, and not go to the next block
    Sending a redraw request will force it to happen as soon as execution of all scripts are finished
"""
class Script:
    def __init__(self):
        self.current_block = None
        self.stepper = None

        self.stack = []

        self.dont_step = False
        self.running = True

        self.status = Enum.STATUS_NONE # This concept is stolen from the VM.

        self.sprite = None

    def is_yielding(self): return (self.status == Enum.STATUS_YIELDED)
    def set_status(self, status_type): 
        self.status = status_type

    #  This concept is once again... DRUMROLL.............. Stolen from the VM!!!!!!
    def branch_to(self, block: str, loop: bool): 
        self.stack.append(StackEntry(block, loop, self.current_block))
        self.dont_step = True
        self.goto(block)

    def goto(self, block: str): 
        if type(block) == Block:
            self.current_block = block
        else:
            self.current_block = self.get_block(block)

    def next_block(self):
        if self.current_block.next:
            self.goto(self.current_block.next)
            return True
        else:
            return False

    def run_block(self, block): 
        return block.run_block(self)
    
    def get_block(self, id):
        return self.stepper.get_block(id)
    
    def kill(self):
        self.running = False

    def step_to_next_block(self):
        could_step = self.next_block()

        if could_step:
            #print("step")
            return # Nothing else needs to happen
        
        if len(self.stack) == 0:  # Stack has no data, stop running thread.
            print("kill")
            self.running = False
            return
        
        stack_last = self.stack.pop()

        if stack_last.is_loop:
            #print("loop")
            """
                i was thinking if its a loop, we store the substacks block in the stack
            """
            self.goto(stack_last.parent)
            return True # now break, as loops need to allow other threads to run.
        else:
            #print("go to next")
            self.goto(stack_last.parent)
            return self.step_to_next_block()

    # Step the script once
    # TODO: we shouldnt need to return to break tbh
    def step_once(self):
        if self.status == Enum.STATUS_YIELDED: # Now that its yielded, step again.
            self.set_status(Enum.STATUS_NONE)

        #print(self.current_block.opcode)
        #print(self.sprite.name)
        #print(self.current_block.id)
        self.run_block(self.current_block)

        should_step = (self.status == Enum.STATUS_NONE) and (not self.dont_step)

        if should_step:
            return self.step_to_next_block()
        elif self.status == Enum.STATUS_YIELDED:
            return True

        self.dont_step = False

    def step(self):
       # print(self.status)

        while True:
            do_break = self.step_once()
            if do_break or (not self.running): break