import pygame

from electrosb3.project import Project

class Window:
    def __init__(self, Project):
        self.project = Project

        pygame.init()

        self.screen = pygame.display.set_mode((480, 360))
        pygame.display.set_caption(self.project.game_name)

    def loop(self, event):
        # Handle events HERE and pass them to the project

        self.project.update(self.screen)

        pass

    def quit(self):
        pygame.quit()