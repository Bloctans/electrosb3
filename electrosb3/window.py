import pygame

from electrosb3.project import Project

class Window:
    def __init__(self, Project):
        self.project = Project

        pygame.init()

        self.screen = pygame.display.set_mode((480, 360))
        pygame.display.set_caption(self.project.game_name)

    def loop(self, event):

        self.screen.fill("white")

        for sprite in self.project.sprites:
            if sprite.visible:
                self.screen.blit(sprite.costumes[0].image, (round(sprite.position.x + 240 - sprite.costumes[0].rotation_center.x),
                                                            round(-sprite.position.y + 180 - sprite.costumes[0].rotation_center.y)))

        self.project.update(self.screen)

        pass

    def quit(self):
        pygame.quit()