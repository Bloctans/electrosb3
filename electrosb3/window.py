import pygame


class Window:

    def __init__(self, window_name):
        self.window_name = window_name

        pygame.init()

        self.screen = pygame.display.set_mode((480, 360))
        pygame.display.set_caption(self.window_name)

    def loop(self, event):
        

        pass

    def quit(self):
        pygame.quit()