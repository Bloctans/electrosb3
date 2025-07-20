import pygame

class Sprite:
    def __init__(self):
        self.costumes = []
        self.current_costume = None

        self.position = pygame.Vector2(0,0)
        self.size = 100
        self.rotation = 90

        self.visible = True
        self.layer_order = 0

        # we can always refactor later
        self.blocks = {}
        self.scripts = []

    def setup(self):
        self.current_costume = self.costumes[0]

    def get_pos(self):
        return self.position - self.current_costume.rotation_center