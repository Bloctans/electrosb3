import pygame

from electrosb3.window import Window
from electrosb3.project import Project

VERSION = "Alpha 1.1"

class Electro:
    def __init__(self):
        print(f"ElectroSB3 Version {VERSION}")

    def run(self, file):
        self.proj = Project(file)

        win = Window(self.proj)
        running = True

        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip()

            win.loop(event)

        win.quit()