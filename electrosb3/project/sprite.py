import pygame

import electrosb3.util as Util

class Sprite:
    def __init__(self):
        self.costumes = []
        self.sounds = []

        self.clones = []
        self.current_costume = None

        self.is_stage = False

        self.position = pygame.Vector2(0,0)
        self.size = 100
        self.rotation = 90

        self.project = None

        self.parent = None

        self.visible = True
        self.layer_order = 0

        self.name = "Placeholder"

        # we can always refactor later
        
    def create_clone(self):
        clone = Sprite()

        clone.position = self.position
        clone.size = self.size
        clone.rotation = self.rotation
        clone.name = self.name
        clone.costumes = self.costumes
        clone.sounds = self.sounds
        clone.current_costume = self.current_costume
        clone.parent = self.parent or self

        self.clones.append(clone)

        stepper = self.project.script_stepper

        def start_clone_hat(hat):
            if hat.sprite == self: stepper.create_script(hat, clone)

        stepper.each_hat("control_start_as_clone", {}, start_clone_hat)

    def delete_this_clone(self): self.parent.delete_clone(self)
    def delete_clone(self, clone): self.clones.pop(self.clones.index(clone))

    def get_stage(self):
        for sprite in self.project.sprites:
            if sprite.is_stage:
                return sprite

    def set_costume(self, costume): 
        if type(costume) == float or type(costume) == int: 
            costume = round(costume)
            costume = self.costumes[costume % len(self.costumes)]

        #print(costume)

        self.current_costume = costume

    def setup(self):
        self.current_costume = self.costumes[0]

    def update(self, screen):
        if self.visible:
            screen.blit(
                self.current_costume.image, 
                Util.to_scratch_pos(self.get_pos())
            )

        for clone in self.clones: clone.update(screen)

    def get_pos(self):
        return self.position - self.current_costume.rotation_center