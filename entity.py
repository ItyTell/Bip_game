import pygame 
import os
from math import floor


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
        self.jump_speed = 5
        self.speed_y = 0
        self.speed = 5 
        Entity.entitys.add(self)

    def load_imgs(self):
        self.idl = []
        path = "imgs\\player"
        self.animation = Animation(path)
        self.image, self.rect = self.animation.get_img()
    
    def move_right(self):
        if self.jumping:
            return
        self.moving_right = True
        self.moving_left = False
        self.animation.change_state('run_right')

    def move_left(self):
        if self.jumping:
            return
        self.moving_right = False 
        self.moving_left = True
        self.animation.change_state('run_left')
    
    def jump(self):
        if  not self.jumping:
            self.speed_y = -self.jump_speed
            self.jumping = True
            self.animation.change_state('jump')

    def land(self):
        if self.jumping:
            self.jumping = False
            self.stop_moving()
            if pygame.key.get_pressed()[pygame.K_d]:
                self.move_right()
            if pygame.key.get_pressed()[pygame.K_a]:
                self.move_left()
        self.speed_y = 0
    
    
    def verticasl_collision(self, obj):
        #pygame.sprite.collide_mask(self, obj)
        if self.rect.colliderect(obj.rect):
            self.rect.bottom = obj.rect.top
            self.land()

    

    def _move(self):
        x, y = self.rect.center
        if self.jumping:
            self.image, self.rect = self.animation.get_img(round(self.speed_y / abs(self.speed_y)) + 2 if abs(self.speed_y) > 1 else 2)
        else:
            self.image, self.rect = self.animation.get_img()
        self.rect.center = (x + self.speed * self.moving_right - self.speed * self.moving_left, y + (self.speed_y + GRAVITY / 2))
        self.speed_y += GRAVITY


    def stop_moving(self):
        if self.jumping:
            return
        self.moving_right = False
        self.moving_left = False
        self.animation.change_state('idl')


    def update(self):
        self._move()


class Animation():

    def __init__(self, path) -> None:
        self.anims = {}
        self.rects = {}
        self.state = 'idl'
        self.speed = 0.25
        self.index = 0
        self._load_anims(path)
        
    def _load_anims(self, path):
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
    

    def get_img(self,  jumping_state = 0):
        """if not jumping, jumping state is 0 else its 1 when starts jumping, 2 when its near the top point and 3 if the entity is falling"""
        if not jumping_state:
            img = self.anims[self.state][floor(self.index)]
            rect = self.rects[self.state][floor(self.index)]
            self.index += self.speed
            self.index -= len(self.anims[self.state]) if self.index >= len(self.anims[self.state]) else 0
        else:
            img = self.anims[self.state][jumping_state - 1]
            rect = self.rects[self.state][jumping_state - 1]
        
        return img, rect

    def change_state(self, state_new):
        if self.state != state_new:
            self.state = state_new
            self.index = 0
