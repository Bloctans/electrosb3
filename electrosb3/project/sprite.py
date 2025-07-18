import pygame

class Sprite:
    def __init__(self):
        self.costumes = []
        self.position = pygame.Vector2(0,0)
        self.size = 100
        self.rotation = 90
        self.visible = True
        self.layer_order = 0