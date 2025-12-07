import electrosb3.block_engine.enum as Enum
import time
import electrosb3.util as Util
import math

from electrosb3.project.sprite import *

import pygame

keymap = {
    "w": pygame.K_w,
    "a": pygame.K_a,
    "s": pygame.K_s,
    "d": pygame.K_d,
    "b": pygame.K_b,
    "x": pygame.K_x,
    "/": pygame.K_SLASH,
    "g": pygame.K_g,
    "space": pygame.K_SPACE,
    "down arrow": pygame.K_DOWN,
    "up arrow": pygame.K_UP,
    "left arrow": pygame.K_LEFT,
    "right arrow": pygame.K_RIGHT
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

    def stop_this_script(self):
        block = None
            
        while True:
            top_stack = self.script.peek_stack()

            if (not top_stack): # No more top stack, kill the thread
                self.script.kill()
                return

            block = self.script.get_block(top_stack.parent)

            if block.get_opcode() == "procedures_call":
                break

            self.script.pop_stack()

        self.script.update_from_stack()

    def get_mutations(self): return self.block.mutations
    def get_stage(self):
        for sprite_name in self.project.sprites:
            sprite = self.get_sprite(sprite_name)
            if sprite.is_stage:
                return sprite
            
    def float(self, num): return Util.to_float(num)
    def int(self, num): return Util.to_int(num)

    def str(self, num):
        if type(num) == float:
            if int(num) == num:
                return str(int(num))
            else:
                return str(num)
        else:
            return str(num)

    def compare(self, num1, num2):
        to_num1 = Util.to_float(num1)
        to_num2 = Util.to_float(num2)

        if Util.can_nan(num1) or Util.can_nan(num2):
            # Handle string compare

            num1 = str(num1).lower()
            num2 = str(num2).lower()

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                return 0

        return to_num1 - to_num2

    def get_sprite(self, name): return self.project.sprites[name]

    def is_touching(self, menu, sprite): 
        return Util.is_touching(menu.name, sprite)

    def start_hats(self, hat, args = None): return self.stepper.start_hats(hat, args)

    def start_timer(self, duration):
        self.timer = time.time()
        self.timer_end = float(duration)
        self.timer_started = True

    def end_timer(self): self.timer_started = False

    def get_store(self, is_variable, sprite):
        if is_variable: return sprite.variables
        else: return sprite.lists

    def get_data(self, data, is_variable):
        id = data.id

        sprite_data = self.get_store(is_variable, self.sprite)
        stage_data = self.get_store(is_variable, self.get_stage())

        if id in sprite_data.keys():
            return sprite_data[id]
        elif id in stage_data.keys():
            return stage_data[id]
        else:
            # this is probably a variable from another sprite, so we just create a new variable in the current sprite
            if is_variable: sprite_data.update({id: Variable([data.name, 0])})
            else: sprite_data.update({id: List([data.name, []])})

            return sprite_data[id]
        
    def variable_from_sprite(self, sprite, name):
        sprite_data = self.get_store(True, sprite)

        for variable_id in sprite_data:
            variable = sprite_data[variable_id]

            if variable.name == name:
                return variable.value

    def get_variable(self, variable): return self.get_data(variable, True)
    def get_list(self, list): return self.get_data(list, False)

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
        if (not self.script.warp): 
            self.script.status = Enum.STATUS_YIELDED
