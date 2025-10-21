from electrosb3.block_engine.script import Script
from electrosb3.block_engine.block import Block
import time
import uuid

class ScriptStepper:
    def __init__(self):
        self.scripts = {}
        self.hats = []
        self.blocks = {}

        self.script_queue = []

        self.redraw_requested = False
        self.inc = 0

    def add_block(self, id, block):
        self.blocks.update({id: block})

    def request_redraw(self):
        #print("Request redraw"+str(self.inc))
        self.inc += 1
        self.redraw_requested = True

    def add_hat(self, hat): self.hats.append(hat)

    def uuid(self): return uuid.uuid4().hex

    def get_block(self, block: str):
        if type(block) == Block:
            return block
        else:
            return self.blocks[block]

    def create_script(self, hat, sprite):
        print("New script")
        print(self.get_block(hat.next))
        script = Script()
        script.current_block = self.get_block(hat.next)
        script.sprite = sprite
        script.stepper = self

        self.script_queue.append({self.uuid(): script})

    def start_hat(self, hat):
        sprite = hat.sprite

        for clone in sprite.clones:
            self.create_script(hat, clone)

        self.create_script(hat, sprite)

    def each_script(self, callback):
        for script in self.scripts:
            callback(script)

    def each_hat(self, opcode, fields, callback):
        #print(self.hats)
        for hat in self.hats:
            if hat.get_opcode() == opcode:
                hat_fields = hat.parse_only_fields()

                cannot_continue = False

                for field in fields:
                    if (not fields[field] == hat_fields[field].name):
                        cannot_continue = True

                if cannot_continue: continue

                # Hard code to only fields for now, as we need to setup thread infustructure for block utils
                callback(hat)

    def start_hats(self, hat, args = {}):
        self.each_hat(hat, args, lambda hat_block: self.start_hat(hat_block))

    def step_hats(self):
        # Go through each hat and run their blocks, if it returns true start a new script
        for hat in self.hats:
            should_run = hat.run_block()

            pass 
            """
                This will not be done for now, as this is rarely used in the actual vm.

                However, when implementing, we need to make sure that we only run if theres a difference between the responses in a frame
                as a hat, from what i know can only start a thread once, before we need to reset it to false next frame to allow another thread to start.
            """

    def step_scripts(self):
        self.redraw_requested = False

        start_time = time.time()

        while (not self.redraw_requested) and (time.time() - start_time < (1/60 * 0.75)):
            to_kill = []

            for script_id in self.scripts:
                script = self.scripts[script_id]

                #print(script.__dict__)

                if (not script.running):
                    to_kill.append(script_id)
                    continue

                #print("Step script")
                script.step()

            for pop in to_kill: self.scripts.pop(pop)

            for script in self.script_queue: self.scripts.update(script)
            self.script_queue = []

        time.sleep(1/30)