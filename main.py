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

# Instancia o gato passando X=100 e Y=400 (e usando G maiúsculo da classe)
gato = gatinho.Gatinho(100, 400)

rodando = True

while rodando:

    clock.tick(60)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    # Atualiza posição e animação
    gato.mover()

    # Limpa a tela
    tela.fill((50, 50, 50))

    # Desenha o personagem
    gato.desenhar(tela)

    # Atualiza o display
    pygame.display.update()

pygame.quit()
sys.exit()