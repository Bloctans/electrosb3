import pygame

from electrosb3.window import Window
from electrosb3.project import Project

class Electro:
    def __init__(self):
        pass

    def run(self, file):
        self.proj = Project(file)

        win = Window(self.proj)
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip()

            win.loop(event)

        win.quit()