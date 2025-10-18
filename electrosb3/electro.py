import pygame

from electrosb3.window import Window
from electrosb3.project import Project

VERSION = "0.4"

class Electro:
    def __init__(self):
        pass

    def run(self, file):
        self.proj = Project(file)

        print()
        print(f"ElectroSB3 {VERSION}")
        print("A Python reimplementation of the Scratch VM, Read the README for more info.")
        print("Originally Created by Touchcreator, Taken over by Bloctans.")
        print("2025")
        print()

        win = Window(self.proj, f"ElectroSB3 {VERSION}")
        running = True

        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip()

            win.loop(event)

        win.quit()