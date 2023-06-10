import pygame
import entity

class Hero(entity.Entity):
    def __init__(self, cords) -> None:
        super().__init__("player", cords)