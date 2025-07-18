import pygame

class Sprite:
    def __init__(self):
        self.costumes = []
        self.position = pygame.Vector2(0,0)
        self.size = 100
        self.rotation = 90
        self.visible = True
        self.layer_order = 0
        self.current_costume = None

    def setup(self):
        self.current_costume = self.costumes[0]

    def get_pos(self):
        return self.position - self.current_costume.rotation_center