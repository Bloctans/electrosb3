from pygame import Vector2, mouse
import math

def to_scratch_pos(Vector2: Vector2):
    x = Vector2.x + 240
    y = (-Vector2.y) + 180

    return (x,y)

def reverse_scratch_pos(Vector2: Vector2):
    x = Vector2.x - 240
    y = (-Vector2.y) + 180

    return (round(x),round(y))

def to_float(num, cant_nan=False):
    try:
        if type(num) == str and num.isalpha():
            if cant_nan: return 0
            else: return "NAN"
        else:
            return float(num or 0)
    except:
        if cant_nan: return 0
        else: return "NAN"
    
def to_int(num, cant_nan=False):
    return int(to_float(num, cant_nan))

def is_touching(menu, sprite):
    sprite1_bounds = sprite.get_bounds()
    cursor = mouse.get_pos()

    if menu == "_mouse_":
        if cursor[0] > sprite1_bounds["x1"] and cursor[0] < sprite1_bounds["x2"]:
            if cursor[1] > sprite1_bounds["y1"] and cursor[1] < sprite1_bounds["y2"]:
                return True

    return False # TODO