import pygame

from electrosb3.renderer.window import Window
from electrosb3.project import Project
from electrosb3.block_engine import Enum as ElectroEnum

VERSION = "0.7"

class Electro:
    def __init__(self, file):
        self.project = Project(file)

        print()
        print(f"ElectroSB3 {VERSION}")
        print("A Python reimplementation of the Scratch VM, Read the README for more info.")
        print("Originally Created by Touchcreator, Taken over by Bloctans.")
        print()

    def start_window(self):
        win = Window(self.project, f"ElectroSB3 {VERSION}")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.project.push_event(ElectroEnum.MOUSE_DOWN)
            
            pygame.display.flip()

            win.loop(event)

        win.quit()