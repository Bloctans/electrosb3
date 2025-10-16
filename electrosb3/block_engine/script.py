import electrosb3.block_engine.enum as Enum
from electrosb3.block_engine.block import Block
from electrosb3.block_engine.block import Block

import time

"""
    Execution flow:
        In a frame, go step through all scripts repeatedly until either a redraw is requested or the thread execution is taking too much time

        one script

"""

class ScriptStepper:
    def __init__(self):
        self.scripts = []

        self.redraw_requested = False
        self.inc = 0

    def request_redraw(self):
        print("Request redraw"+str(self.inc))
        self.inc += 1
        self.redraw_requested = True

    def add_script(self, script):
        self.scripts.append(script)

    def step_scripts(self):
        self.redraw_requested = False

        start_time = time.time()

        while (not self.redraw_requested) and (time.time() - start_time < (1/60 * 0.75)):
            for script in self.scripts:
                #print("Step script")
                script.step()

class StackEntry:
    def __init__(self, block, is_loop):
        self.block = block
        self.is_loop = is_loop

"""
    Yielding will stop the thread dead in its tracks, and not go to the next block
    Sending a redraw request will force it to happen as soon as execution of all scripts are finished
"""
class Script:
    def __init__(self):
        self.current_block = None
        self.start_block = None
        self.script_stepper = None

        self.stack = []

        self.running = False
        self.status = Enum.STATUS_NONE # This concept is stolen from the VM.

        self.sprite = None

    def is_yielding(self): return (self.status == Enum.STATUS_YIELDED)
    def set_status(self, status_type): 
        self.status = status_type

    #  This concept is once again... DRUMROLL.............. Stolen from the VM!!!!!!
    def branch_to(self, block: str, loop: bool): 
        self.goto(block) # we should be able to directly branch, hopefully, maybe, potentially.
        self.stack.append(StackEntry(self.current_block, loop))

    def goto(self, block: str): 
        if type(block) == Block:
            self.current_block = block
        else:
            self.current_block = self.get_block(block)

    def step_to_next_block(self):
        if self.current_block.next:
            self.goto(self.current_block.next)
            return True
        else:
            return False
        #print(self.current_block.opcode)

    def run_block(self, block): 
        return block.run_block(self)
    
    def request_redraw(self): self.script_stepper.request_redraw()
    
    def get_block(self, id): 
        if not (id in self.sprite.blocks):
            debug_block = self.sprite.debug_blocks[id]

            print(f"Couldn't get block! Missing opcode {debug_block["opcode"]}, fields: {debug_block["fields"]}, inputs: {debug_block["inputs"]}")

        return self.sprite.blocks[id]

    # Step the script once
    # TODO: we shouldnt need to return to break tbh
    def step_once(self):
        if self.status == Enum.STATUS_YIELDED: # Now that its yielded, step again.
            self.set_status(Enum.STATUS_NONE)

        #print(self.current_block.opcode)
        self.run_block(self.current_block)

        #if self.step_next: # Stop to the custom step if it exists
        #    self.goto(self.step_next)
        #    self.step_next = None

        if self.status == Enum.STATUS_NONE:
            could_step = self.step_to_next_block()

            if could_step:
                return # Nothing else needs to happen
            
            if len(self.stack) == 0:  # Stack has no data, stop running thread.
                print("kill thread")
                self.running = False
                return True
            
            stack_last = self.stack.pop()

            if stack_last.is_loop:
                print("loop")
                """
                    i was thinking if its a loop, we store the substacks block in the stack
                """
                self.branch_to(stack_last.block, True)
                #self.just_branched = True
                #self.goto(stack_last.block)
                return True # now break, as loops need to allow other threads to run.
            else:
                print("go to next")
                self.goto(stack_last.block)
                self.step_to_next_block()
        elif self.status == Enum.STATUS_YIELDED:
            return True
        else:
            print("INVALID STATUS")

    def step(self):
       # print(self.status)

        if (not self.running):
            self.current_block = self.start_block
            hat_result = self.run_block(self.current_block)
            if hat_result: 
                self.running = True
                self.step_to_next_block()
        else:
            while True:
                do_break = self.step_once()
                if do_break: break