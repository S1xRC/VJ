"""
Hola este es modulo Bug,
este modulo manejara la creacion y acciones de los Bugs
"""
import pygame
import random
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load('assets\bug.png')
BUGpng_scaled = pygame.transform.scale(BUGpng,(64,64))

class Enemy(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Enemy, self).__init__()
        self.surf=BUGpng_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect=self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 100,
                random.randint(0,SCREEN_HEIGHT),
            )
        )
        self.speed=random,randint(3,5)
        pass
    pass

    def update(self):
        pass