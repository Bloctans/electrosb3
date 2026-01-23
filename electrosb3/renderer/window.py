import pygame

class Window:
    def __init__(self, Project, Title):
        self.project = Project

        pygame.init()

        self.screen = pygame.display.set_mode((480, 360))
        pygame.display.set_caption(f"{Title} - \"{self.project.game_name}\"")

    def loop(self, event):
        self.screen.fill("white")

        self.project.update(self.screen)

    def quit(self):
        pygame.quit()