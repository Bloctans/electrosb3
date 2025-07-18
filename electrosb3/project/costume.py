import io
from pygame import Vector2, image

class Costume:
    def __init__(self, image_file, rotation_center: tuple, name: str):
        if type(image_file) == str:
            self.image = image.load(io.BytesIO(image_file.encode()))
        else:
            self.image = image.load(io.BytesIO(image_file))
        self.rotation_center = Vector2(rotation_center[0], rotation_center[1])
        self.name = name