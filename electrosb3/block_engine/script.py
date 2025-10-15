import electrosb3.block_engine.enum as Enum
from electrosb3.block_engine.block import Block
from electrosb3.block_engine.block import Block

from time import sleep as wait_blocking

class ScriptStepper:
    def __init__(self):
        self.scripts = []

        self.redraw_requested = False

    def request_redraw(self):
        self.redraw_requested = True

    def add_script(self, script):
        self.scripts.append(script)

    def step_scripts(self):
        self.redraw_requested = False

        while (not self.redraw_requested):
            for script in self.scripts:
                if script.status == Enum.STATUS_YIELDED: # Now that its yielded, step again.
                    self.set_status(Enum.STATUS_NONE)
                elif script.status == Enum.STATUS_NONE: # Step thread normally
                    script.step()
                elif script.status == Enum.STATUS_DONE: # Done, no need to step thread
                    continue

        for script in self.scripts:
            script.set_status(Enum.STATUS_NONE)

class Script:
    def __init__(self):
        self.current_block = None
        self.start_block = None

        self.step_next = None # Value set by a block that determines what to step to next

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
        self.step_next = block
        self.stack.append([self.current_block, loop])

    def goto(self, block: str): 
        if type(block) == Block:
            self.current_block = block
        else:
            self.current_block = self.get_block(block)

    def step_block(self):
        #print(self.current_block.opcode)
        if self.step_next: # Stop to the custom step if it exists
            self.goto(self.step_next)
            self.step_next = None
        elif self.current_block.next == None: # Stop the script if there is no next
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
    
    def request_redraw(self): self.script_stepper.request_redraw()
    
    def get_block(self, id): 
        if not (id in self.sprite.blocks):
            debug_block = self.sprite.debug_blocks[id]

            print(f"Couldn't get block! Missing opcode {debug_block["opcode"]}, fields: {debug_block["fields"]}, inputs: {debug_block["inputs"]}")

        return self.sprite.blocks[id]

    """
        New idea (From vm)

        Run until we have either done a full frame or a redraw is requested (do we need frame yield?)
    """
    def step(self):
       # print(self.status)

        if (not self.running):
            self.current_block = self.start_block
            hat_result = self.run_block(self.current_block)
            if hat_result: 
                self.running = True
                self.step_block()
        else:
            print(self.current_block.opcode)
            oldstatus = self.status

            self.run_block(self.current_block)
            self.step_block()
            
            if oldstatus == self.status:
                self.set_status(Enum.STATUS_DONE)