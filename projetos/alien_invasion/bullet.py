import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #classe para gerenciar os projeteis disparados pela espaçonave

    def __init__(self, ai_game): #toda classe relacionada ao fluxo principal do jogo precisa do parametro ai_game
        #cria um objeto bullet na posição atual da espaçonave
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #cria um bullet rect em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #armazena a posição do projétil como um float
        self.y = float(self.rect.y)

    def update(self):
        #desloca o projetil verticalmente pela tela
        #atualiza a posição exata do projétil

        self.y -= self.settings.bullet_speed

        #atualiza a posicao do rect

        self.rect.y = self.y

    def draw_bullet(self):

        #desenha o projétil na tela
        pygame.draw.rect(self.screen, self.color, self.rect)