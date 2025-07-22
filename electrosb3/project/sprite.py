import pygame

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
        self.scripts = []

    def costume_from_name(self, name):
        for costume in self.costumes:
            if costume.name == name: return costume

    def sound_from_name(self, name):
        for sound in self.sounds:
            if sound.name == name: return sound
            
    def set_costume(self, costume): self.current_costume = costume

    def setup(self):
        self.current_costume = self.costumes[0]

    def get_pos(self):
        return self.position - self.current_costume.rotation_center