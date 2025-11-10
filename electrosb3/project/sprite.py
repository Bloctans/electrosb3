import pygame
import math

import electrosb3.util as Util

class Variable:
    def __init__(self, variable):
        self.name = variable[0]
        self.value = variable[1]

    def copy(self):
        return Variable([self.name, self.value])
    
class List:
    def __init__(self, variable):
        self.name = variable[0]
        self.list: list = variable[1]

    def get_length(self):
        return len(self.list)
    
    def can_get(self, index):
        return self.get_length() > int(index)

    def get_item(self, index):
        index = Util.to_int(index)

        return self.can_get(index) and self.list[int(index)] or 0
    
    def add(self, item):
        self.list.append(item)

    def number_of(self, number):
        if number in self.list:
            return self.list.index(number)+1
        else:
            return 0
        
    def insert_at(self, index, item):
        self.list.insert(int(index), item)

    def clear(self):
        self.list = []
        
    def replace(self, index, item):
        self.list[int(index)-1] = item

import uuid

class Sprite:
    def __init__(self):
        self.costumes = []
        self.sounds = []

        self.variables = {}
        self.lists = {}

        self.clones = []
        self.current_costume = None

        self.id = self.uuid()

        self.is_stage = False

        self.position = pygame.Vector2(0,0)
        self.size = 100
        self.rotation = 90

        self.alpha = 0

        self.project = None
        self.renderer = None

        self.parent = None

        self.visible = True
        self.layer_order = 0

        self.t = 0

        self.name = "Placeholder"

        # we can always refactor later

    def uuid(self): return uuid.uuid4().hex

    def set_layer(self, layer):
        self.layer_order = layer

    def copy_variables(self):
        variables = {}

        for variable in self.variables: variables.update({variable: self.variables[variable].copy()})

        return variables
        
    def copy_lists(self):
        lists = {}

        for list in self.lists: lists.update({list: self.lists[list].copy()})

        return lists
    
    def get_main_sprite(self):
        return self.parent or self
    
    def create_clone(self):
        clone = Sprite()

        parent = self.get_main_sprite()

        clone.layer_order = self.layer_order + 1
        clone.position = self.position.copy()
        clone.id = self.uuid()
        clone.size = self.size
        clone.rotation = self.rotation
        clone.name = self.name
        clone.costumes = self.costumes
        clone.sounds = self.sounds
        clone.current_costume = self.current_costume
        clone.parent = parent
        clone.renderer = self.renderer
        clone.lists = self.copy_lists()
        clone.variables = self.copy_variables()
        clone.project = self.project

        parent.clones.append(clone)
        self.renderer.add(clone)

        stepper = self.project.script_stepper

        def start_clone_hat(hat):
            if hat.sprite == parent: 
                stepper.create_script(hat, clone)

        stepper.each_hat("control_start_as_clone", {}, start_clone_hat)

    def delete_this_clone(self): 
        if self.parent:
            self.parent.delete_clone(self.id)
        else:
            print("attempt to delete parent")

    def delete_clone(self, id): 
        stepper = self.project.script_stepper

        for clone in self.clones:
            if clone.id == id:
                self.clones.remove(clone)
                self.renderer.remove(clone)

                def kill_threads(script):
                    if script.sprite.id == id:
                        script.kill()

                stepper.each_script(kill_threads)
                break

    def costume_from_name(self, name):
        for costume in self.costumes:
            if costume.name == name: return costume

    def set_costume(self, costume): 
        to_num = Util.to_float(costume)

        if not (to_num == "NAN"): 
            costume = int(to_num)
            costume = round(costume)-1
            costume = self.costumes[costume % len(self.costumes)]

        if type(costume) == str:
            costume = self.costume_from_name(costume)

        self.current_costume = costume

    def get_image(self):
        image = self.current_costume.image

        center = self.get_pos()

        transformed_size = self.size/100

        if self.rotation == 0:
            rotated_image = image
        else:
            rotated_image = pygame.transform.rotate(image, self.rotation+90)

        rotated_image = pygame.transform.scale_by(rotated_image, (transformed_size, transformed_size))

        rotated_image.set_alpha(255-self.alpha)

        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = (center[0], center[1])).center)

        return rotated_image, new_rect

    def get_bounds(self):
        _, rect = self.get_image()

        return {
            "x1": rect[0],
            "y1": rect[1],
            "x2": rect[0] + rect[2],
            "y2": rect[1] + rect[3]
        }

    def setup(self):
        self.current_costume = self.costumes[0]

    def update(self, screen):
        self.t += 1
        
    def get_pos(self):
        return Util.to_scratch_pos(self.position - self.current_costume.rotation_center)