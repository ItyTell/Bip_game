import pygame
import entity

class Player(entity.Entity):
    def __init__(self, cords) -> None:
        super().__init__("player", cords)
    
    def check_keys(self):
        if pygame.key.get_pressed()[pygame.K_d]:
            self.move_right()
        if pygame.key.get_pressed()[pygame.K_a]:
            self.move_left()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.jump()