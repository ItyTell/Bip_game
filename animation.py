import os
import pygame
from math import floor


class Animation():

    def __init__(self, path) -> None:
        files = os.listdir(path)
        files.sort(key=len) 
        self.imgs = []
        self.rects = []
        for file in files:
            img = pygame.image.load(path + "\\" + file).convert_alpha()
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            img.set_colorkey((0, 0, 0))
            self.imgs.append(img)
            self.rects.append(img.get_rect())
    
    def __len__(self):
        return len(self.imgs)
    
    def get_frame(self, index):
        return self.imgs[index], self.rects[index]



class Animation_controller():

    def __init__(self, entity, path) -> None:
        self.anims = {}
        self.state = 'idl'
        self.speed = 0.25
        self.index = 0
        self.entity = entity
        self._load_anims(path)
        
    def _load_anims(self, path):
        animations = os.listdir(path= path)
        for animation in animations:
            self.anims[animation] = Animation(path + "\\" + animation)
            
    def get_img(self,  jumping_state = 0):
        """if not jumping, jumping state is 0 else its 1 when starts jumping, 2 when its near the top point and 3 if the entity is falling"""
        if 'land' in self.state:
            img, rect = self.anims[self.state].get_frame(floor(self.index))
            self.index += self.speed
            if floor(self.index) > len(self.anims[self.state]) - 1:
                self.change_state('idl'); self.entity.stop_landing()

        elif not ('jump' in self.state):
            img, rect = self.anims[self.state].get_frame(floor(self.index))
            self.index += self.speed
            self.index -= len(self.anims[self.state]) if self.index >= len(self.anims[self.state]) else 0

        elif 'jump' in self.state:
            index = (round(self.entity.speed_y / abs(self.entity.speed_y)) + 2 if abs(self.entity.speed_y) > 1 else 2) - 1
            img, rect = self.anims[self.state].get_frame(floor(index))
        
        return img, rect

    def change_state(self, state_new):
        if self.state != state_new:
            self.state = state_new
            self.index = 0