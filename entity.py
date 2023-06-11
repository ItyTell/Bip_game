import pygame 
import os
from math import floor

class Entity(pygame.sprite.Sprite):

    entitys = pygame.sprite.Group()

    def __init__(self, name, cords) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_imgs()
        self.rect.center = cords 
        self.moving_right = False
        self.moving_left = False
        self.speed = 5 
        Entity.entitys.add(self)

    def load_imgs(self):
        self.idl = []
        path = "imgs\\player"
        self.animation = Animation(path)
        self.image, self.rect = self.animation.get_img()
    
    def move_right(self):
        self.moving_right = True
        self.moving_left = False
        self.animation.change_state('run')

    def stop_moving(self):
        self.moving_right = False
        self.moving_left = False
        self.animation.change_state('idl')


    def update(self, screen):
        x, y = self.rect.center
        self.image, self.rect = self.animation.get_img()
        self.rect.center = (x + self.speed * self.moving_right - self.speed * self.moving_left, y)


class Animation():

    def __init__(self, path) -> None:
        self.anims = {}
        self.rects = {}
        self.state = 'idl'
        self.speed = 0.25
        self.index = 0
        animations = os.listdir(path= path)
        for animation in animations:
            files = os.listdir(path= path + "\\" + animation)
            files.sort(key=len) 
            imgs = []
            rects = []
            for file in files:
                img = pygame.image.load(path + "\\" + animation + "\\" + file).convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
                img.set_colorkey((0, 0, 0))
                imgs.append(img)
                rects.append(img.get_rect())
            self.anims[animation] = imgs
            self.rects[animation] = rects

    def get_img(self):
        img = self.anims[self.state][floor(self.index)]
        rect = self.rects[self.state][floor(self.index)]
        self.index += self.speed
        self.index -= len(self.anims[self.state]) if self.index >= len(self.anims[self.state]) else 0
        return img, rect

    def change_state(self, state_new):
        self.state = state_new
        self.index = 0
