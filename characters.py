import pygame

class Hero:

    def __init__(self, cords) -> None:
        self.load_imgs()
        self.cords = cords 

    def load_imgs(self):
        self.img = pygame.image.load('imgs\\bip1.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.img.get_width()*3, self.img.get_height()*3))
        self.img.set_colorkey((0, 0, 0))
