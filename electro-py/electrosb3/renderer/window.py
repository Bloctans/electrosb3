import pygame

class Window:
    def __init__(self, Project, Title):
        self.project = Project

        pygame.init()

        self.screen = pygame.display.set_mode((480, 360))
        pygame.display.set_caption(f"{Title} - \"{self.project.game_name}\"")

        self.font = pygame.font.SysFont("Consolas", 12)

    def loop(self, event):
        self.screen.fill("white")

        self.project.update(self.screen)

        info = self.project.get_info()
        y = 0

        for i in info:
            self.screen.blit(self.font.render(i+": "+str(info[i]), True, (128,128,128)), (0, y))
            y += 12

    def quit(self):
        pygame.quit()