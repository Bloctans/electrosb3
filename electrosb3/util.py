from pygame import Vector2, mouse
import math

def to_scratch_pos(Vector2: Vector2):
    x = Vector2.x + 240
    y = (-Vector2.y) + 180

    return (x,y)

def index(list, index):
    try:
        return list[index]
    except IndexError:
        return None

def reverse_scratch_pos(Vector2: Vector2):
    x = Vector2.x - 240
    y = (-Vector2.y) + 180

    return (round(x),round(y))

def to_float(num):  
    if num == "":
        return 0.0
    elif type(num) == str and (not is_numeric(num)):
        return 0.0       
    elif type(num) == str or type(num) == int or type(num) == float:
        return float(num)
    else:
        return 0.0
    
def is_numeric(num):
    try:
        float(num)
        return True
    except:
        return False

def to_int(num):
    return int(to_float(num))

def is_touching(menu, sprite):
    sprite1_bounds = sprite.get_bounds()
    cursor = mouse.get_pos()

    if menu == "_mouse_":
        if cursor[0] > sprite1_bounds["x1"] and cursor[0] < sprite1_bounds["x2"]:
            if cursor[1] > sprite1_bounds["y1"] and cursor[1] < sprite1_bounds["y2"]:
                return True

    return False # TODO