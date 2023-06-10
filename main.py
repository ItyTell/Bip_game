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
        self.hero = Hero([15, 400])
        self.run()
    
    def load_settings(self) -> None:
        with open('settings.json') as file:
            settings = json.loads(file.read())
        self.screen_params = (settings["screen"]["width"], settings["screen"]["height"])
        file.close()
    
    def drew(self):
        for entity in Entity.entitys:
            entity.update(self.screen)

    def run(self):
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.screen.fill("purple")
            self.drew()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()



Game()
