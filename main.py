import pygame 
import moderngl
import json 
import os

from characters import *
from entity import *
from pygame.locals import *

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
                if event.type == pygame.KEYDOWN:
                    if event.key == K_d:
                        self.hero.move_right()
                if event.type == pygame.KEYUP:
                    if event.key == K_d:
                        self.hero.stop_moving()

            self.draw()
            self.clock.tick(60)
        
        
        pygame.quit()




Game()


