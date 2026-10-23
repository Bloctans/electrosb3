import pygame
import time
import math

class Drawer:
    def __init__(self):
        self.drawables = []

    def get_highest_layer(self):
        return len(self.drawables)

    def sort_drawables(self): 
        self.drawables.sort(key = lambda a: a.layer_order)

    def add(self, object):
        self.drawables.append(object)

    def remove(self, object):
        self.drawables.remove(object)

    def update(self, screen: pygame.Surface):
        self.sort_drawables()

        for drawable in self.drawables:
            if drawable.visible:
                if drawable.redraw: 
                    drawable.redraw_sprite()

                image, rect = drawable.get_image()

                #pygame.draw.rect(screen, (255,0,0), rect, 2)

                screen.blit(
                    image, 
                    rect
                )

        pygame.draw.rect(screen, (255,0,0), (0, 50+math.sin(time.time())*50, 50, 50), 2)