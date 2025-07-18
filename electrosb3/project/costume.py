import io
from pygame import Vector2, image

class Costume:
    def __init__(self):
        self.image = None
        self.rotation_center = Vector2(0,0)
        self.name = "Placeholder"