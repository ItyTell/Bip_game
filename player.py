import pygame
import entity

class Player(entity.Entity):
    def __init__(self, cords) -> None:
        super().__init__("player", cords)