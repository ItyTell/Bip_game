import pygame 
import moderngl
import json 
import os

from player import *
from entity import *
from pygame.locals import *

pygame.init()


#path
BACKGROUND_PATH = r"C:\Users\nickk\Bip_game\imgs\background"


class Game:

    def __init__(self) -> None:
        self.load_settings()
        self.screen = pygame.display.set_mode(self.screen_params); self.clock = pygame.time.Clock()    
        self.player = Player([40, 400])
        self.ground = Ground(-10000, 740, 100000, 50) # -inf downspot +inf some_nomber = 50 (just not 0) 

        self.background = pygame.image.load(BACKGROUND_PATH + r"\desert\background.png").convert_alpha()

        bakcground_scale = 0.75

        self.background = pygame.transform.scale(self.background, (self.background.get_width() * bakcground_scale, 
                                                                   self.background.get_height() * bakcground_scale))

        self.background.set_colorkey((0, 0, 0))
        self.background_rect = self.background.get_rect()
        self.background_rect.center = [i / 2 for i in self.screen_params]


        self.run()
    
    def load_settings(self) -> None:
        with open('settings.json') as file:
            settings = json.loads(file.read())
        self.screen_params = (settings["screen"]["width"], settings["screen"]["height"])
        self.fps = settings["fps"]
        file.close()
    
    def draw(self):
        Entity.entitys.update()
        self.player.verticasl_collision(self.ground)
        self.screen.blit(self.background, self.background_rect)
        Entity.entitys.draw(self.screen)
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
            self.clock.tick(self.fps)
        
        
        pygame.quit()




Game()


