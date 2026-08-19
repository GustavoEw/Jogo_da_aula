import pygame

class Gatinho:  # Nome da classe em maiúsculo por convenção
    def __init__(self, x, y):
        # Características principais do personagem
        self.x = x
        self.y = y
        self.hp = 100
        self.power = 10
        self.speed = 5
        self.gravidade = 0.8
        self.velocidade_y = 0
        self.pulo = False
        self.olhandodireita = True

        # Definindo as dimensões e retângulo do personagem
        self.sprite_width = 64
        self.sprite_height = 64 
        self.rect = pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)

        # Carregando animação de corrida
        self.animacao_correr = []
        for i in range(1, 7):  # Ajustado para 1 até 6 (sua imagem tinha 6 frames de corrida)
            sprite = pygame.image.load(f"icons/correr_padrao/frame_{i}.png").convert_alpha()
            sprite = pygame.transform.scale(sprite, (self.sprite_width, self.sprite_height))
            self.animacao_correr.append(sprite)  

        # Controle de Animação
        self.animacao_index = 0
        self.animacao_tempo = 0 
        self.imagem_atual = self.animacao_correr[0]

    def correr(self):
        # Avança o contador de tempo
        self.animacao_tempo += 1
        if self.animacao_tempo >= 5:  # Troca de frame a cada 5 ticks
            self.animacao_index += 1
            if self.animacao_index >= len(self.animacao_correr):
                self.animacao_index = 0
            self.animacao_tempo = 0

        # Atualiza a imagem atual
        self.imagem_atual = self.animacao_correr[self.animacao_index]

    def desenhar(self, tela):
        # Copia a imagem atual
        sprite = self.imagem_atual

        # Se estiver olhando para a esquerda, inverte horizontalmente
        if not self.olhandodireita:
            sprite = pygame.transform.flip(sprite, True, False)

        # Desenha na tela usando o retângulo de posição
        tela.blit(sprite, (self.x, self.y))