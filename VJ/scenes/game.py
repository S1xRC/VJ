'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy


def StartScene():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1024  # revisar ancho de la imagen de fondo
    SCREEN_HEIGHT = 768  # revisar alto de la imagen de fondo

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    background_image = pygame.image.load("assets\pixelBackground.jpg").convert()

    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = None
    ''' 2.- generador de enemigos'''

    ADDENEMY = None

    ''' 3.- creamos la instancia de jugador'''
    player = None

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = None
    all_sprites = None

    ''' hora de hacer el gameloop '''
    running=True

    while running:
        screen.blit(background_image,[0,0])
            
        for event in pygame.event.get():

            if event.type==KEYDOWN:

                if event.key==K_ESCAPE:
                    running=False
            
            elif event.type==QUIT:
                running=False
        pygame.display.flip()