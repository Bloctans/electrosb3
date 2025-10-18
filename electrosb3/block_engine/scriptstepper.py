from electrosb3.block_engine.script import Script
import time

class ScriptStepper:
    def __init__(self):
        self.scripts = []
        self.hats = []

        self.redraw_requested = False
        self.inc = 0

    def request_redraw(self):
        #print("Request redraw"+str(self.inc))
        self.inc += 1
        self.redraw_requested = True

    def add_hat(self, hat): self.hats.append(hat)

    def create_script(self, hat):
        script = Script()
        script.current_block = hat.next
        script.sprite = hat.sprite
        script.script_stepper = self

        self.scripts.append(script)

    def each_hat(self, opcode, fields, callback):
        #print(self.hats)
        for hat in self.hats:
            if hat.get_opcode() == opcode:
                hat_fields = hat.parse_only_fields()

                if fields:
                    for field in fields:
                        print(field, hat_fields[field])
                        #if field == hat_fields[field]

                # Hard code to only fields for now, as we need to setup thread infustructure for block utils
                callback(hat)

    def start_hats(self, hat, args):
        self.each_hat(hat, args, lambda hat_block: self.create_script(hat_block))

    def start_hats(self, hat):
        self.each_hat(hat, None, lambda hat_block: self.create_script(hat_block))

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
            for script in self.scripts:
                #print("Step script")
                script.step()

        time.sleep(1/30)