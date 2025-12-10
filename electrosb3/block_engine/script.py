import electrosb3.block_engine.enum as Enum
from electrosb3.block_engine.block import Block
import electrosb3.util as util

class StackFrame:
    def __init__(self, stack_parent, is_loop, is_procedure, warp):
        self.parent = stack_parent

        self.is_loop = is_loop

        self.warp = warp
        self.is_procedure = is_procedure

        self.params = {}

"""
    Yielding will stop the thread dead in its tracks, and not go to the next block
    Sending a redraw request will force it to happen as soon as execution of all scripts are finished
"""
class Script:
    def __init__(self):
        self.start_block = None
        self.hat = None

        self.stepper = None
        self.sprite = None

        self.current_block = None

        self.stack = []
        self.data = {}

        self.warp = False
        self.procedure = False

        self.dont_step = False
        self.running = True

        self.status = Enum.STATUS_NONE # This concept is stolen from the VM

    #  This concept is once again... DRUMROLL.............. Stolen from the VM!!!!!!
    def branch_to(self, block: str, loop: bool, procedure: bool = False, procedure_warp: bool = False): 
        if (not block): 
            print("Cant branch")
            return
         
        if (not self.warp):
            self.warp = procedure_warp

        entry = StackFrame(self.current_block, loop, procedure, procedure_warp)

        self.stack.append(entry)

        self.dont_step = True # TODO: Could we just run step_once() instead of needing dont_step?
        self.goto(block)

        return entry

    # Another concept from vm... man i feel so stupid sometimes...
    def get_procedure_params(self): 
        stack = self.next_stack_procedure()

        #print(self.stack)

        if stack:
            return stack.params
        else:
            return None

    def peek_stack(self): return util.index(self.stack, -1)
    def copy_stack(self): return self.stack.copy()
    def pop_stack(self): return self.stack.pop()

    def restart(self):
        self.goto(self.start_block)
        self.stack = []
        self.warp = False
        self.dont_step = False
        self.status = Enum.STATUS_NONE

    def goto(self, block: str): 
        if type(block) == Block:
            self.current_block = block
        else:
            self.current_block = self.get_block(block)

    # Goto the next stack block if it exists
    def next_block(self):
        if self.current_block.next:
            self.goto(self.current_block.next)
            return True
        else:
            return False

    def run_block(self, block): return block.run_block(self)
    def get_block(self, id): return self.stepper.get_block(id)
    
    def kill(self):
        #self.hat.scripts.remove(self)
        self.running = False

    # Update the current block based off the top stack
    def update_from_stack(self):
        self.goto(self.peek_stack().parent)
        self.step_to_next_block()

    def next_stack_procedure(self):
        temp_stack = self.copy_stack()

        while True:
            if len(temp_stack) < 1:
                return False

            next_procedure = temp_stack.pop()

            if next_procedure and next_procedure.is_procedure:
                return next_procedure

    # Step to the next block (in stack or not)
    def step_to_next_block(self):
        could_step = self.next_block()

        if could_step:
            #print("step")
            return # Nothing else needs to happen
        
        if len(self.stack) == 0:  # Stack has no data, kill thread.
            #print("kill")
            self.kill()
            return
        
        # We couldnt simply step to the next block, so go look at the stack now
        stack_last = self.stack.pop()

        # This will signify we are exiting a custom block
        if stack_last.is_procedure:
            next_procedure = self.next_stack_procedure()

            if next_procedure:
                self.warp = next_procedure.warp
            else:
                #print("unwarp")
                # Procedure stack finally run dry
                self.warp = False
                self.procedure = False

        if stack_last.is_loop:
            #print("loop")
            # If its a loop, we go back to whatever called it and rerun that block
            self.goto(stack_last.parent)
            return True # now break, as loops need to allow other threads to run.
        else:
            #print("go to next")
            # If its not a loop, we go to whatever called it, then do step_to_next_block() recursively
            self.goto(stack_last.parent)
            return self.step_to_next_block()

    # Step the script once
    # TODO: we shouldnt need to return to break tbh
    def step_once(self):
        if self.status == Enum.STATUS_YIELDED: # Now that its yielded, step again.
            self.status = Enum.STATUS_NONE

        self.run_block(self.current_block)

        should_step = (self.status == Enum.STATUS_NONE) and (not self.dont_step)
        do_break = False

        if should_step:
            do_break = self.step_to_next_block()
        elif self.status == Enum.STATUS_YIELDED:
            do_break = True
        else:
            self.dont_step = False

        #if (not self.warp):
        return do_break

    def step(self):
        while True:
            do_break = self.step_once()
            
            if do_break or (not self.running): break