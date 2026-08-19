import pygame, sys
from pygame.locals import *
import os

import gatinho

# Initialize Pygame

pygame.init()

# Cria a janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption("Meu Primeiro Jogo")

# Relógio para controlar o FPS
clock = pygame.time.Clock()

    
gato = gatinho.gatinho()

rodando = True

while rodando:

    clock.tick(60)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    gato.mover()

    tela.fill((50, 50, 50))

    gato.desenhar(tela)

    pygame.display.update()

pygame.quit()