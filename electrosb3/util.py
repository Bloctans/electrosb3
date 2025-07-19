from pygame import Vector2

def to_scratch_pos(Vector2: Vector2):
    x = Vector2.x + 240
    y = (-Vector2.y) + 180

    return (x,y)