import pygame 
import moderngl
import json 
import os

from player import *
from entity import *
from pygame.locals import *

pygame.init()


class Game:

    def __init__(self) -> None:
        self.load_settings()
        self.screen = pygame.display.set_mode(self.screen_params)
        self.clock = pygame.time.Clock()    
        self.player = Player([40, 400])
        self.ground = Ground(0, 500, 1000, 100)
        self.run()
    
    def load_settings(self) -> None:
        with open('settings.json') as file:
            settings = json.loads(file.read())
        self.screen_params = (settings["screen"]["width"], settings["screen"]["height"])
        file.close()
    
    def draw(self):
        self.screen.fill("purple")
        Entity.entitys.update()
        self.player.verticasl_collision(self.ground)
        Entity.entitys.draw(self.screen)
        self.ground.draw(self.screen)
        pygame.display.flip()

    def check_keys(self):

        self.player.check_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
            if event.type == pygame.KEYUP:
                if event.key == K_d or event.key == K_a:
                    self.player.stop_moving()


    def run(self):
        self.run = True
        while self.run:
            self.check_keys()
            self.draw()
            self.clock.tick(60)
        
        
        pygame.quit()




Game()


