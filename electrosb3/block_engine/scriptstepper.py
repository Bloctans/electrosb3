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
        self.inc += 1
        self.redraw_requested = True

    def add_hat(self, hat): self.hats.append(hat)

    def uuid(self): return uuid.uuid4().hex

    def get_block(self, block: str):
        if type(block) == Block:
            return block
        elif block in self.blocks.keys():
            return self.blocks[block]

    def create_script(self, hat, sprite):
        #print("New script")
        if hat.next:
            script = Script()
            script.hat = hat
            script.start_block = self.get_block(hat.next)
            script.current_block = script.start_block
            script.sprite = sprite
            script.stepper = self

            hat.scripts.append(script)

            self.script_queue.append({self.uuid(): script})

    def create_hat_scripts(self, hat, sprite):
        for clone in sprite.clones:
            self.create_script(hat, clone)

        self.create_script(hat, sprite)

    # TODO: an each_hat in clone mode may help shorten this script
    def start_hat(self, hat):
        sprite = hat.sprite.get_main_sprite()

        if ("restart_existing" in hat.info.keys()):
            threads_exist = []

            def restart_threads(script): 
                if script.hat == hat:
                    threads_exist.append(script.sprite.id)
                    script.restart()

            self.each_script(restart_threads)

            def create_if_none(thesprite):
                if not (thesprite.id in threads_exist): self.create_script(hat, thesprite)

            create_if_none(sprite)
            for clone in sprite.clones: create_if_none(clone)
        else:
            for clone in sprite.clones: self.create_script(hat, clone)
            self.create_script(hat, sprite)

    def each_script(self, callback):
        for script in self.scripts:
            callback(self.scripts[script])

    def each_hat(self, opcode, fields, callback, clones=False):
        for hat in self.hats:
            if hat.get_opcode() == opcode:
                hat_fields = hat.parse_only_fields()

                cannot_continue = False

                for field in fields:
                    if (not fields[field] == hat_fields[field].name):
                        cannot_continue = True

                if cannot_continue: continue

                sprite = hat.sprite

                # Hard code to only fields for now, as we need to setup thread infustructure for block utils
                if clones:
                    for clone in sprite.clones: callback(hat, clone)
                    callback(hat, sprite)
                else:
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

                if (not script.running):
                    to_kill.append(script_id)
                    continue

                script.step()

            for pop in to_kill: self.scripts.pop(pop)

            for script in self.script_queue: self.scripts.update(script)
            self.script_queue = []

        while (time.time() - start_time < (1/25)): pass