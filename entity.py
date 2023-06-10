import pygame 
import os
from math import floor

class Entity:
    entitys = []

    def __init__(self, name, cords) -> None:
        self.name = name
        self.load_imgs()
        self.cords = cords 
        self.anim_index = 0
        self.anim_speed = 0.25
        Entity.entitys.append(self)

    def load_imgs(self):
        self.idl = []
        path = "imgs"
        for i in range(10):
            img = pygame.image.load(path + "\\" + self.name + "_idl" + str(i + 1) + ".bmp").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            img.set_colorkey((0, 0, 0))
            self.idl.append(img)

    def update(self, screen):
        screen.blit(self.idl[floor(self.anim_index)], self.cords)
        self.anim_index += self.anim_speed
        self.anim_index -= len(self.idl) if self.anim_index >= len(self.idl) else 0
