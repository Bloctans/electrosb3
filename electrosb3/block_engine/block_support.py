import electrosb3.block_engine.enum as Enum
import time

import pygame

keymap = {
    "w": pygame.K_w,
    "a": pygame.K_a,
    "s": pygame.K_s,
    "d": pygame.K_d,
    "space": pygame.K_SPACE
}

class API:
    def __init__(self, sprite, block):
        self.script = None
        self.stepper = None

        self.sprite = sprite
        self.block = block

        self.info = {}

        self.timer = 0
        self.timer_end = 0
        self.timer_started = False

        self.loops = 0

    #def wait_frame(self): self.script.set_yield(Enum.YIELD_TILL_NEXT_FRAME)

    def is_key_down(self, key): return pygame.key.get_pressed()[keymap[key]]

    def start_hats(self, hat, args = None): self.stepper.start_hats(hat, args)

    def start_timer(self, duration):
        self.timer = time.time()
        self.timer_end = float(duration)
        self.timer_started = True

    def end_timer(self): self.timer_started = False

    def timer_finished(self): 
        return (time.time() - self.timer) > self.timer_end

    def request_redraw(self):
        self.stepper.request_redraw()

    def set_script(self, script): 
        self.script = script
        self.stepper = self.script.script_stepper

    def do_yield(self): self.script.set_status(Enum.STATUS_YIELDED)
