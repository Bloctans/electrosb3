import pygame

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

    def update(self, screen):
        self.sort_drawables()
        for drawable in self.drawables:
            if drawable.visible:
                image, rect = drawable.get_image()

                pygame.draw.rect(screen, (255,0,0), rect, 2)

                screen.blit(
                    image, 
                    rect
                )