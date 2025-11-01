from pygame import Vector2

def to_scratch_pos(Vector2: Vector2):
    x = Vector2.x + 240
    y = (-Vector2.y) + 180

    return (x,y)

def reverse_scratch_pos(Vector2: Vector2):
    x = Vector2.x - 240
    y = (-Vector2.y) + 180

    return (round(x),round(y))

def to_float(num):
    if type(num) == str and num.isspace():
        return 0
    else:
        return float(num or 0)
    
def to_int(num):
    return int(to_float(num))