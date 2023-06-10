import pygame 
import os
from math import floor

class Entity(pygame.sprite.Sprite):

    entitys = pygame.sprite.Group()

    def __init__(self, name, cords) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_imgs()
        self.rect = self.image.get_rect()
        self.rect.center = cords 
        Entity.entitys.add(self)

    def load_imgs(self):
        self.idl = []
        path = "imgs\\player"
        self.animation = Animation(path)
        self.image = self.animation.anims["idl"][0]

    def update(self, screen):
        self.image = self.animation.get_img()
        cords = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = cords


class Animation():

    def __init__(self, path) -> None:
        self.anims = {}
        self.state = 'idl'
        self.speed = 0.25
        self.index = 0
        animations = os.listdir(path= path)
        for animation in animations:
            files = os.listdir(path= path + "\\" + animation)
            files.sort(key=len) 
            imgs = []
            for file in files:
                img = pygame.image.load(path + "\\" + animation + "\\" + file).convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
                img.set_colorkey((0, 0, 0))
                imgs.append(img)
            self.anims[animation] = imgs
    def get_img(self):
        img = self.anims[self.state][floor(self.index)]
        self.index += self.speed
        self.index -= len(self.anims[self.state]) if self.index >= len(self.anims[self.state]) else 0
        return img
