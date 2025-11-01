import electrosb3.block_engine.enum as Enum
import time
import electrosb3.util as Util

from electrosb3.project.sprite import *

import pygame

keymap = {
    "w": pygame.K_w,
    "a": pygame.K_a,
    "s": pygame.K_s,
    "d": pygame.K_d,
    "b": pygame.K_b,
    "space": pygame.K_SPACE,
    "down arrow": pygame.K_DOWN,
    "up arrow": pygame.K_UP
}

class API:
    def __init__(self, block):
        self.script = None
        self.stepper = None

        self.sprite = None
        self.block = block
        self.project = None

        self.info = {}

        self.timer = 0
        self.timer_end = 0
        self.timer_started = False

        self.loops = 0

    def is_key_down(self, key): 
        if key == "any":
            for key in pygame.key.get_pressed():
                if key:
                    return True
                
            return False
        else:
            return pygame.key.get_pressed()[keymap[key]]
        
    def get_script_info(self): return self.script.data

    def get_cursor(self): return Util.reverse_scratch_pos(pygame.Vector2(pygame.mouse.get_pos()))
    def get_mouse_down(self): return pygame.mouse.get_pressed()[0]

    def get_mutations(self): return self.block.mutations
    def get_stage(self):
        for sprite_name in self.project.sprites:
            sprite = self.get_sprite(sprite_name)
            if sprite.is_stage:
                return sprite
            
    def float(self, num): return Util.to_float(num)
    def int(self, num): return Util.to_int(num)

    def get_sprite(self, name): return self.project.sprites[name]

    def is_touching(self, menu, sprite): 
        sprite1_bounds = sprite.get_bounds()
        cursor = self.get_cursor()

        if menu.name == "_mouse_":
            #if cursor[0] > sprite1_bounds["x1"] and cursor[0] < sprite1_bounds["x2"]:
            if cursor[1] > sprite1_bounds["y1"] and cursor[1] < sprite1_bounds["y2"]:
                print("Mouse2")
                return True

        return False # TODO

    def start_hats(self, hat, args = None): self.stepper.start_hats(hat, args)

    def start_timer(self, duration):
        self.timer = time.time()
        self.timer_end = float(duration)
        self.timer_started = True

    def end_timer(self): self.timer_started = False

    def get_variable(self, id):
        sprite_vars = self.sprite.variables
        stage_vars = self.get_stage().variables

        if id in sprite_vars.keys():
            return sprite_vars[id]
        elif id in stage_vars.keys():
            return stage_vars[id]
        else:
            # this is probably a variable from another sprite, but we just create a new variable in the current sprite anyways since i dont wanna do through more pain
            sprite_vars.update({id: Variable(["unknown", 0])})

            return sprite_vars[id]

    def get_list(self, id):
        sprite_lists = self.sprite.lists
        stage_lists = self.get_stage().lists

        if id in sprite_lists.keys():
            return sprite_lists[id]
        elif id in stage_lists.keys():
            return stage_lists[id]
        else:
            # this is probably a list from another sprite, but we just create a new list in the current sprite anyways since i dont wanna do through more pain
            sprite_lists.update({id: List(["unknown", []])})

            return sprite_lists[id]

    def timer_finished(self): 
        return (time.time() - self.timer) >= self.timer_end

    def request_redraw(self):
        if (not self.script.warp): self.stepper.request_redraw()

    def configure(self, script): 
        sprite = script.sprite

        self.script = script
        self.sprite = sprite
        self.project = sprite.project
        self.stepper = self.script.stepper

    def do_yield(self): 
        if (not self.script.warp): self.script.set_status(Enum.STATUS_YIELDED)
