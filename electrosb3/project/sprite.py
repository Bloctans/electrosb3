import pygame

import electrosb3.util as Util

class Sprite:
    def __init__(self):
        self.costumes = []
        self.sounds = []
        self.current_costume = None

        self.position = pygame.Vector2(0,0)
        self.size = 100
        self.rotation = 90

        self.visible = True
        self.layer_order = 0

        self.name = "Placeholder"

        # we can always refactor later
        self.blocks = {}
        self.debug_blocks = {}
            
    def set_costume(self, costume): 
        print(costume)

        if type(costume) == float or type(costume) == int: 
            costume = round(costume)
            costume = self.costumes[costume % (len(self.costumes)-1)]

        print(costume)

        self.current_costume = costume

    def setup(self):
        self.current_costume = self.costumes[0]

    def update(self, screen):
        if self.visible:
            screen.blit(
                self.current_costume.image, 
                Util.to_scratch_pos(self.get_pos())
            )
            #print("rendering "+self.current_costume.name)

    def get_pos(self):
        return self.position - self.current_costume.rotation_center