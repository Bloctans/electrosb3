import electrosb3.block_engine.enum as Enum
import time

class API:
    def __init__(self, sprite, block):
        self.script = None
        self.sprite = sprite
        self.block = block

        self.timer = 0
        self.timer_end = 0
        self.timer_started = False

        self.loops = 0

    def wait_frame(self): self.script.set_yield(Enum.YIELD_TILL_NEXT_FRAME)

    def start_timer(self, duration):
        self.timer = time.time()
        self.timer_end = duration
        self.timer_started = True

    def end_timer(self): self.timer_started = False

    def timer_finished(self): 
        print((time.time() - self.timer))
        return (time.time() - self.timer) > self.timer_end

    def set_script(self, script): self.script = script

    def do_yield(self): self.script.set_yield(Enum.YIELD)

    def stop_yield(self): 
        self.end_timer()
        self.script.set_yield(Enum.YIELD_NONE)
