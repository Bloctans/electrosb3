import pygame

from electrosb3.window import Window
from electrosb3.project import Project

class Electro:
    def __init__(self):
        pass

    def run(self, file):
        self.proj = Project(file)

        win = Window(self.proj.game_name)
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            bg = pygame.image.load("./unpacked/" + self.proj.data["targets"][0]["costumes"][0]["md5ext"])
            # setting bg color to white
            win.screen.fill("white")
            win.screen.blit(bg, bg.get_rect(center = win.screen.get_rect().center))
            
            pygame.display.flip()


            win.loop(event)

        win.quit()