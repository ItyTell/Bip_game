import pygame 
import os
from math import floor
from animation import *

GRAVITY = 0.25


class Ground(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
    


    def draw(self, screen):
        pygame.draw.rect(screen, 'blue', self.rect)




class Entity(pygame.sprite.Sprite):

    entitys = pygame.sprite.Group()

    def __init__(self, name, cords) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_imgs()
        self.rect.center = cords 
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.landing = False
        self.jump_speed = 10
        self.speed_y = 0
        self.speed = 10 
        Entity.entitys.add(self)

    def load_imgs(self):
        self.idl = []
        path = "imgs\\player"
        self.animation = Animation_controller(self, path)
        self.image, self.rect = self.animation.get_img()
    
    def move_right(self):
        if self.jumping or self.landing:
            return
        self.moving_right = True
        self.moving_left = False
        self.animation.change_state('run_right')

    def move_left(self):
        if self.jumping or self.landing:
            return
        self.moving_right = False 
        self.moving_left = True
        self.animation.change_state('run_left')
    
    def jump(self):
        if  self.jumping or self.landing:
            return
        self.speed_y = -self.jump_speed
        self.jumping = True
        self.animation.change_state('jump_right')
        if self.moving_left:
            self.animation.change_state('jump_left')


    def land(self):
        if self.jumping:
            self.jumping = False
            self.landing = True
            self.animation.change_state('land_left' if self.moving_left else 'land_right')
            self.moving_right = False
            self.moving_left = False
        self.speed_y = 0
    
    def stop_landing(self):
        self.landing = False

    
    
    def verticasl_collision(self, obj):
        #pygame.sprite.collide_mask(self, obj)
        if self.rect.colliderect(obj.rect):
            self.rect.bottom = obj.rect.top
            self.land()

    

    def _move(self):
        x, y = self.rect.center
        if self.jumping:
            self.image, self.rect = self.animation.get_img()
        else:
            self.image, self.rect = self.animation.get_img()
        self.rect.center = (x + self.speed * self.moving_right - self.speed * self.moving_left, y + (self.speed_y + GRAVITY / 2))
        self.speed_y += GRAVITY


    def stop_moving(self):
        if self.jumping or self.landing:
            return
        self.moving_right = False
        self.moving_left = False
        self.animation.change_state('idl')


    def update(self):
        self._move()
