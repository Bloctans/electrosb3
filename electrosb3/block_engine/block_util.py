# Block utilities - Shared functions between blocks

import pygame

keymap = {
    "w": pygame.K_w,
    "a": pygame.K_a,
    "s": pygame.K_s,
    "d": pygame.K_d,
    "space": pygame.K_SPACE
}

def is_key_down(key):
    return pygame.key.get_pressed()[keymap[key]]