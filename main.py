import pygame 
import moderngl
import json 
import os

from characters import *
from entity import *


pygame.init()


class Game:

    def __init__(self) -> None:
        self.load_settings()
        self.screen = pygame.display.set_mode(self.screen_params)
        self.clock = pygame.time.Clock()    
        self.hero = Hero([40, 400])
        self.run()
    
    def load_settings(self) -> None:
        with open('settings.json') as file:
            settings = json.loads(file.read())
        self.screen_params = (settings["screen"]["width"], settings["screen"]["height"])
        file.close()
    
    def draw(self):
        self.screen.fill("purple")
        Entity.entitys.update(self.screen)
        Entity.entitys.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.draw()
            self.clock.tick(60)
        pygame.quit()



Game()


